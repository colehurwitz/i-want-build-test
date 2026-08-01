#!/usr/bin/env python3
"""Parse eval output and compute pass rates per agent and tier.

Usage:
    python scripts/parse-eval-results.py --output-dir eval/output --agents-dir agents
    python scripts/parse-eval-results.py --output-dir eval/output --agents-dir agents --tier easy
    python scripts/parse-eval-results.py --output-dir eval/output --agents-dir agents --agent hr_people_ops/employee_directory
"""
import argparse
import json
import os
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
    """Parse eval output directory and compute pass rates per agent."""
    results = {}

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


def format_baseline_summary(results: dict, agents_dir: Path, tier_filter: str = None) -> str:
    lines = ["# Baseline Evaluation Summary\n"]
    lines.append("| Agent | Tier | Tests | Passed | Pass Rate | Expected Range | In Range |")
    lines.append("|-------|------|-------|--------|-----------|----------------|----------|")

    for key, data in sorted(results.items()):
        parts = key.split("/")
        category, agent_name = parts[0], parts[1]
        tier = get_agent_tier(agents_dir, category, agent_name)

        if tier_filter and tier != tier_filter:
            continue

        expected = EXPECTED_RANGES.get(tier, (0, 100))
        in_range = expected[0] <= data["pass_rate"] <= expected[1]
        range_str = f"{expected[0]}-{expected[1]}%"
        status = "YES" if in_range else "**NO**"

        lines.append(
            f"| {key} | {tier} | {data['total']} | {data['passed']} | "
            f"{data['pass_rate']}% | {range_str} | {status} |"
        )

    return "\n".join(lines)


def format_delta_comparison(baseline: dict, optimized: dict, agents_dir: Path) -> str:
    lines = ["# Delta Comparison: Baseline vs Optimized\n"]
    lines.append("| Agent | Tier | Baseline | Optimized | Delta | Expected Delta | Match |")
    lines.append("|-------|------|----------|-----------|-------|----------------|-------|")

    for key in sorted(set(baseline.keys()) & set(optimized.keys())):
        parts = key.split("/")
        category, agent_name = parts[0], parts[1]
        tier = get_agent_tier(agents_dir, category, agent_name)

        b_rate = baseline[key]["pass_rate"]
        o_rate = optimized[key]["pass_rate"]
        delta = round(o_rate - b_rate, 1)

        expected_delta = EXPECTED_DELTAS.get(tier, (0, 100))
        delta_str = f"{expected_delta[0]}-{expected_delta[1]}%"
        match = expected_delta[0] <= delta <= expected_delta[1]
        match_str = "YES" if match else "**NO**"

        lines.append(
            f"| {key} | {tier} | {b_rate}% | {o_rate}% | "
            f"{'+' if delta >= 0 else ''}{delta}% | {delta_str} | {match_str} |"
        )

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Parse eval results")
    parser.add_argument("--output-dir", required=True, help="Path to eval/output")
    parser.add_argument("--agents-dir", required=True, help="Path to agents/")
    parser.add_argument("--tier", help="Filter by tier")
    parser.add_argument("--agent", help="Filter by agent (category/name)")
    parser.add_argument("--format", choices=["table", "json"], default="table")
    parser.add_argument("--baseline-dir", help="Baseline output dir for delta comparison")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    agents_dir = Path(args.agents_dir)

    if not output_dir.exists():
        print(f"ERROR: Output directory does not exist: {output_dir}", file=sys.stderr)
        sys.exit(1)

    results = parse_eval_output(output_dir)

    if not results:
        print("WARNING: No eval results found in output directory", file=sys.stderr)
        sys.exit(1)

    if args.baseline_dir:
        baseline = parse_eval_output(Path(args.baseline_dir))
        print(format_delta_comparison(baseline, results, agents_dir))
    else:
        if args.format == "json":
            print(json.dumps(results, indent=2))
        else:
            print(format_baseline_summary(results, agents_dir, args.tier))


if __name__ == "__main__":
    main()
