#!/usr/bin/env python3
"""Generate synthetic eval results for testing the analysis pipeline.

Creates realistic metadata.json files simulating eval output with pass rates
matching expected tier ranges (with some variance).
"""
import json
import os
import random
import sys
from pathlib import Path

TIER_AGENTS = {
    "easy": [
        "hr_people_ops/employee_directory",
        "it_service_mgmt/access_provisioner",
        "it_service_mgmt/password_reset_agent",
        "customer_sales/lead_qualifier",
        "supply_chain/shipping_coordinator",
        "supply_chain/inventory_tracker",
        "customer_sales/lead_qualifier",
    ],
    "medium": [
        "hr_people_ops/leave_manager",
        "hr_people_ops/payroll_processor",
        "it_service_mgmt/incident_commander",
        "customer_sales/deal_pipeline",
        "customer_sales/customer_support",
        "supply_chain/order_fulfillment",
        "compliance_risk/data_privacy_officer",
        "compliance_risk/audit_trail_reviewer",
    ],
    "hard": [
        "it_service_mgmt/service_desk_agent",
        "hr_people_ops/onboarding_coordinator",
        "customer_sales/account_manager",
        "compliance_risk/security_incident_responder",
        "compliance_risk/regulatory_compliance_checker",
        "supply_chain/vendor_manager",
        "finance_procurement/procurement_agent",
    ],
}

BASELINE_RANGES = {
    "easy": (0.25, 0.45),
    "medium": (0.45, 0.65),
    "hard": (0.65, 0.85),
}

OPTIMIZED_DELTAS = {
    "easy": (0.30, 0.50),
    "medium": (0.20, 0.30),
    "hard": (0.10, 0.20),
}


def generate_metadata(pass_score: bool, test_name: str) -> dict:
    score = random.uniform(0.7, 1.0) if pass_score else random.uniform(0.0, 0.4)
    return {
        "test_case": test_name,
        "journey_success": {"score": score},
        "status": "success" if pass_score else "failed",
    }


def generate_results(output_dir: Path, mode: str = "baseline"):
    random.seed(42 if mode == "baseline" else 99)

    for tier, agents in TIER_AGENTS.items():
        seen = set()
        for agent_path in agents:
            if agent_path in seen:
                continue
            seen.add(agent_path)

            agent_dir = output_dir / agent_path
            agent_dir.mkdir(parents=True, exist_ok=True)

            n_tests = random.randint(3, 6)
            base_rate = random.uniform(*BASELINE_RANGES[tier])

            if mode == "optimized":
                delta = random.uniform(*OPTIMIZED_DELTAS[tier])
                target_rate = min(base_rate + delta, 1.0)
            else:
                target_rate = base_rate

            n_pass = round(n_tests * target_rate)
            n_pass = max(0, min(n_pass, n_tests))

            results = [True] * n_pass + [False] * (n_tests - n_pass)
            random.shuffle(results)

            for i, passed in enumerate(results):
                test_name = f"test_case_{i+1}"
                metadata = generate_metadata(passed, test_name)
                with open(agent_dir / f"{test_name}.metadata.json", "w") as f:
                    json.dump(metadata, f, indent=2)


def main():
    if len(sys.argv) < 2:
        print("Usage: generate-synthetic-results.py <output_dir> [baseline|optimized]")
        sys.exit(1)

    output_dir = Path(sys.argv[1])
    mode = sys.argv[2] if len(sys.argv) > 2 else "baseline"
    generate_results(output_dir, mode)
    print(f"Generated {mode} results in {output_dir}")


if __name__ == "__main__":
    main()
