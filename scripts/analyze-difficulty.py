#!/usr/bin/env python3
"""Analyze difficulty verification results and recommend reclassifications.

Reads baseline and optimized eval output, computes deltas, checks for
reclassification triggers, and generates a comprehensive report.

Usage:
    python scripts/analyze-difficulty.py \
        --baseline-dir results/baseline-output \
        --optimized-dir eval/output \
        --agents-dir agents \
        --output results/difficulty-verification-report.md
"""
import argparse
import json
import sys
from pathlib import Path


EXPECTED_RANGES = {
    "easy": (30, 40),
    "medium": (50, 60),
    "hard": (70, 80),
}

EXPECTED_DELTAS = {
    "easy": (30, 50),
    "medium": (20, 30),
    "hard": (10, 20),
}


def get_agent_tier(agents_dir: Path, category: str, agent_name: str) -> str:
    test_cases_dir = agents_dir / category / agent_name / "test_cases"
    tiers = set()
    if test_cases_dir.exists():
        for tc_file in test_cases_dir.glob("*.json"):
            with open(tc_file) as f:
                tc = json.load(f)
            for tag in tc.get("tags", []):
                if tag.startswith("optimization_difficulty:"):
                    tiers.add(tag.split(":")[1])
    if len(tiers) == 1:
        return tiers.pop()
    return ",".join(sorted(tiers)) if tiers else "unknown"


def parse_eval_output(output_dir: Path) -> dict:
    results = {}
    if not output_dir.exists():
        return results

    for category_dir in sorted(output_dir.iterdir()):
        if not category_dir.is_dir():
            continue
        category = category_dir.name

        for agent_dir in sorted(category_dir.iterdir()):
            if not agent_dir.is_dir():
                continue
            agent_name = agent_dir.name
            key = f"{category}/{agent_name}"

            total = 0
            passed = 0

            for result_file in agent_dir.glob("*.metadata.json"):
                with open(result_file) as f:
                    metadata = json.load(f)
                total += 1
                journey_success = metadata.get("journey_success", {})
                if isinstance(journey_success, dict):
                    score = journey_success.get("score", 0)
                elif isinstance(journey_success, (int, float)):
                    score = journey_success
                else:
                    score = 0
                if score >= 0.5:
                    passed += 1

            if total == 0:
                for csv_file in agent_dir.glob("summary_metrics.csv"):
                    import csv
                    with open(csv_file) as f:
                        reader = csv.DictReader(f)
                        for row in reader:
                            total += 1
                            js = float(row.get("journey_success", 0))
                            if js >= 0.5:
                                passed += 1

            if total > 0:
                results[key] = {
                    "total": total,
                    "passed": passed,
                    "pass_rate": round(passed / total * 100, 1),
                }

    return results


def check_reclassification(
    agent_key: str, tier: str, baseline_rate: float, delta: float
) -> list:
    triggers = []
    expected_range = EXPECTED_RANGES.get(tier, (0, 100))
    expected_delta = EXPECTED_DELTAS.get(tier, (0, 100))

    range_low, range_high = expected_range
    if baseline_rate < range_low - 20 or baseline_rate > range_high + 20:
        triggers.append(
            f"Baseline {baseline_rate}% is 20%+ outside expected range "
            f"{range_low}-{range_high}%"
        )

    return triggers


def generate_report(
    baseline: dict, optimized: dict, agents_dir: Path
) -> str:
    lines = []
    lines.append("# Difficulty Verification Report\n")
    lines.append("## 1. Tier-Level Baseline Summary\n")

    tier_data = {"easy": [], "medium": [], "hard": []}
    for key, data in baseline.items():
        parts = key.split("/")
        tier = get_agent_tier(agents_dir, parts[0], parts[1])
        if tier in tier_data:
            tier_data[tier].append(data["pass_rate"])

    lines.append("| Tier | Agents | Mean | Min | Max | Expected Range | Status |")
    lines.append("|------|--------|------|-----|-----|----------------|--------|")
    for tier in ["easy", "medium", "hard"]:
        rates = tier_data[tier]
        if rates:
            mean = round(sum(rates) / len(rates), 1)
            mn = min(rates)
            mx = max(rates)
            expected = EXPECTED_RANGES[tier]
            in_range = expected[0] <= mean <= expected[1]
            status = "IN RANGE" if in_range else "OUT OF RANGE"
            lines.append(
                f"| {tier.upper()} | {len(rates)} | {mean}% | {mn}% | "
                f"{mx}% | {expected[0]}-{expected[1]}% | {status} |"
            )
        else:
            lines.append(f"| {tier.upper()} | 0 | - | - | - | - | NO DATA |")

    lines.append("\n## 2. Delta Comparison\n")
    lines.append("| Agent | Tier | Baseline | Optimized | Delta | Expected | Match |")
    lines.append("|-------|------|----------|-----------|-------|----------|-------|")

    sample_agents = set(baseline.keys()) & set(optimized.keys())
    deltas_by_tier = {"easy": [], "medium": [], "hard": []}

    for key in sorted(sample_agents):
        parts = key.split("/")
        tier = get_agent_tier(agents_dir, parts[0], parts[1])
        b_rate = baseline[key]["pass_rate"]
        o_rate = optimized[key]["pass_rate"]
        delta = round(o_rate - b_rate, 1)

        if tier in deltas_by_tier:
            deltas_by_tier[tier].append(delta)

        expected = EXPECTED_DELTAS.get(tier, (0, 100))
        match = expected[0] <= delta <= expected[1]
        match_str = "YES" if match else "**NO**"

        lines.append(
            f"| {key} | {tier} | {b_rate}% | {o_rate}% | "
            f"{'+' if delta >= 0 else ''}{delta}% | "
            f"{expected[0]}-{expected[1]}% | {match_str} |"
        )

    lines.append("\n## 3. Delta Ordering Check\n")
    easy_deltas = deltas_by_tier.get("easy", [])
    medium_deltas = deltas_by_tier.get("medium", [])
    hard_deltas = deltas_by_tier.get("hard", [])

    easy_mean = sum(easy_deltas) / len(easy_deltas) if easy_deltas else 0
    medium_mean = sum(medium_deltas) / len(medium_deltas) if medium_deltas else 0
    hard_mean = sum(hard_deltas) / len(hard_deltas) if hard_deltas else 0

    lines.append(f"- EASY mean delta: {easy_mean:.1f}%")
    lines.append(f"- MEDIUM mean delta: {medium_mean:.1f}%")
    lines.append(f"- HARD mean delta: {hard_mean:.1f}%")
    lines.append("")

    ordering_correct = easy_mean > medium_mean > hard_mean
    if ordering_correct:
        lines.append(
            "**PASS**: EASY delta > MEDIUM delta > HARD delta — "
            "difficulty classifications are validated."
        )
    else:
        lines.append(
            "**FAIL**: Delta ordering is inverted — "
            "difficulty classifications may need revision."
        )
        if easy_mean <= medium_mean:
            lines.append("  - EASY delta <= MEDIUM delta (expected EASY > MEDIUM)")
        if medium_mean <= hard_mean:
            lines.append("  - MEDIUM delta <= HARD delta (expected MEDIUM > HARD)")

    lines.append("\n## 4. Reclassification Analysis\n")

    reclassifications = []
    for key, data in baseline.items():
        parts = key.split("/")
        tier = get_agent_tier(agents_dir, parts[0], parts[1])
        if tier not in EXPECTED_RANGES:
            continue

        triggers = check_reclassification(key, tier, data["pass_rate"], 0)

        if key in optimized:
            delta = optimized[key]["pass_rate"] - data["pass_rate"]
            expected_delta = EXPECTED_DELTAS[tier]
            if delta < expected_delta[0] - 10 or delta > expected_delta[1] + 10:
                triggers.append(
                    f"Delta {delta:.1f}% far outside expected "
                    f"{expected_delta[0]}-{expected_delta[1]}%"
                )

        if triggers:
            reclassifications.append({
                "agent": key,
                "current_tier": tier,
                "baseline": data["pass_rate"],
                "triggers": triggers,
            })

    if reclassifications:
        lines.append("| Agent | Current Tier | Baseline | Triggers | Recommendation |")
        lines.append("|-------|-------------|----------|----------|----------------|")
        for r in reclassifications:
            trigger_str = "; ".join(r["triggers"])
            b = r["baseline"]
            tier = r["current_tier"]
            if b > EXPECTED_RANGES[tier][1] + 20:
                rec = "Consider HARDER tier"
            elif b < EXPECTED_RANGES[tier][0] - 20:
                rec = "Consider EASIER tier"
            else:
                rec = "Review needed"
            lines.append(
                f"| {r['agent']} | {tier} | {b}% | {trigger_str} | {rec} |"
            )
    else:
        lines.append("No reclassification triggers detected. All agents within expected ranges.")

    lines.append("\n## 5. Conclusion\n")
    if ordering_correct and not reclassifications:
        lines.append(
            "The empirical data validates the current EASY/MEDIUM/HARD classification system. "
            "Baseline pass rates fall within expected ranges and optimization deltas follow "
            "the expected ordering (EASY > MEDIUM > HARD)."
        )
    elif not ordering_correct:
        lines.append(
            "The delta ordering does not match expectations. The classification system "
            "needs revision — some agents may be assigned to the wrong difficulty tier."
        )
    else:
        lines.append(
            "While delta ordering is correct, some individual agents show baseline rates "
            "outside expected ranges. These agents should be reviewed for potential "
            "reclassification."
        )

    return "\n".join(lines)


def update_test_case_tags(agents_dir: Path, agent_key: str, new_tier: str):
    parts = agent_key.split("/")
    category, agent_name = parts[0], parts[1]
    test_cases_dir = agents_dir / category / agent_name / "test_cases"

    for tc_file in test_cases_dir.glob("*.json"):
        with open(tc_file) as f:
            tc = json.load(f)

        updated = False
        for i, tag in enumerate(tc.get("tags", [])):
            if tag.startswith("optimization_difficulty:"):
                tc["tags"][i] = f"optimization_difficulty:{new_tier}"
                updated = True

        if updated:
            with open(tc_file, "w") as f:
                json.dump(tc, f, indent=4)
                f.write("\n")


def main():
    parser = argparse.ArgumentParser(description="Analyze difficulty verification")
    parser.add_argument("--baseline-dir", required=True)
    parser.add_argument("--optimized-dir", required=True)
    parser.add_argument("--agents-dir", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--apply-reclassify", action="store_true",
                        help="Actually update test case tags if reclassification needed")
    args = parser.parse_args()

    baseline = parse_eval_output(Path(args.baseline_dir))
    optimized = parse_eval_output(Path(args.optimized_dir))
    agents_dir = Path(args.agents_dir)

    report = generate_report(baseline, optimized, agents_dir)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(report)

    print(report)


if __name__ == "__main__":
    main()
