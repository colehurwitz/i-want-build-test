#!/usr/bin/env bash
set -euo pipefail

# Run evaluation for all agents in a given difficulty tier.
# Usage: ./scripts/eval-tier.sh <easy|medium|hard>

if [ $# -lt 1 ]; then
  echo "Usage: $0 <easy|medium|hard>"
  exit 1
fi

TIER="$1"

case "$TIER" in
  easy|medium|hard) ;;
  *) echo "ERROR: Invalid tier '$TIER'. Must be: easy, medium, hard"; exit 1 ;;
esac

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
AGENTS_DIR="$PROJECT_ROOT/agents"
OUTPUT_BASE="$PROJECT_ROOT/eval/output"
ENV_FILE="${ENV_FILE:-$PROJECT_ROOT/.env}"

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
SKIPPED=()

mkdir -p "$OUTPUT_BASE"

for domain in "${DOMAINS[@]}"; do
  domain_dir="$AGENTS_DIR/$domain"
  [ ! -d "$domain_dir" ] && continue

  for agent_dir in "$domain_dir"/*/; do
    [ ! -d "$agent_dir" ] && continue
    agent_name="$(basename "$agent_dir")"
    test_cases_dir="$agent_dir/test_cases"

    if [ ! -d "$test_cases_dir" ] || [ -z "$(ls -A "$test_cases_dir" 2>/dev/null)" ]; then
      continue
    fi

    # Check if any test case in this agent matches the tier
    if ! grep -rl "optimization_difficulty:$TIER" "$test_cases_dir" >/dev/null 2>&1; then
      SKIPPED+=("$domain/$agent_name")
      continue
    fi

    # Create a temp directory with only test cases matching the tier
    tier_tmp=$(mktemp -d)
    trap "rm -rf $tier_tmp" EXIT
    for tc_file in "$test_cases_dir"/*.json; do
      if grep -q "optimization_difficulty:$TIER" "$tc_file" 2>/dev/null; then
        cp "$tc_file" "$tier_tmp/"
      fi
    done

    if [ -z "$(ls -A "$tier_tmp" 2>/dev/null)" ]; then
      SKIPPED+=("$domain/$agent_name")
      rm -rf "$tier_tmp"
      continue
    fi

    output_dir="$OUTPUT_BASE/$domain/$agent_name"
    mkdir -p "$output_dir"

    echo ""
    echo "--- Evaluating ($TIER tier): $domain/$agent_name ---"
    if orchestrate evaluations evaluate \
      -p "$tier_tmp" \
      -o "$output_dir" \
      -e "$ENV_FILE"; then
      SUCCEEDED+=("$domain/$agent_name")
    else
      echo "  ERROR: Evaluation failed for $domain/$agent_name"
      FAILED+=("$domain/$agent_name")
    fi
    rm -rf "$tier_tmp"
  done
done

echo ""
echo "========================================="
echo "   TIER EVALUATION SUMMARY: $TIER"
echo "========================================="
echo "Evaluated: ${#SUCCEEDED[@]}"
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
