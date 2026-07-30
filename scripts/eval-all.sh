#!/usr/bin/env bash
set -euo pipefail

# Run evaluations for all agents and produce a summary report.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
AGENTS_DIR="$PROJECT_ROOT/agents"
OUTPUT_BASE="$PROJECT_ROOT/eval/output"
ENV_FILE="${ENV_FILE:-$PROJECT_ROOT/.env}"
CONFIG_FILE="${CONFIG_FILE:-$PROJECT_ROOT/eval/configs/eval_config.yaml}"

DOMAINS=(
  hr_people_ops
  it_service_mgmt
  finance_procurement
  customer_sales
  supply_chain
  compliance_risk
)

FAILED=()
SUCCEEDED=()

mkdir -p "$OUTPUT_BASE"

for domain in "${DOMAINS[@]}"; do
  domain_dir="$AGENTS_DIR/$domain"
  [ ! -d "$domain_dir" ] && continue

  for agent_dir in "$domain_dir"/*/; do
    [ ! -d "$agent_dir" ] && continue
    agent_name="$(basename "$agent_dir")"
    test_cases_dir="$agent_dir/test_cases"

    if [ ! -d "$test_cases_dir" ] || [ -z "$(ls -A "$test_cases_dir" 2>/dev/null)" ]; then
      echo "SKIP: No test cases for $domain/$agent_name"
      continue
    fi

    output_dir="$OUTPUT_BASE/$domain/$agent_name"
    mkdir -p "$output_dir"

    echo ""
    echo "--- Evaluating: $domain/$agent_name ---"
    if orchestrate evaluations evaluate \
      -c "$CONFIG_FILE" \
      -p "$test_cases_dir" \
      -o "$output_dir" \
      -e "$ENV_FILE"; then
      SUCCEEDED+=("$domain/$agent_name")
    else
      echo "  ERROR: Evaluation failed for $domain/$agent_name"
      FAILED+=("$domain/$agent_name")
    fi
  done
done

echo ""
echo "========================================="
echo "         EVALUATION SUMMARY"
echo "========================================="
echo "Succeeded: ${#SUCCEEDED[@]}"
for s in "${SUCCEEDED[@]}"; do
  echo "  ✓ $s"
done

if [ ${#FAILED[@]} -gt 0 ]; then
  echo ""
  echo "Failed: ${#FAILED[@]}"
  for f in "${FAILED[@]}"; do
    echo "  ✗ $f"
  done
fi

echo ""
echo "Results saved to: $OUTPUT_BASE"
