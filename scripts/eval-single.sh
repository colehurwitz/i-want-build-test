#!/usr/bin/env bash
set -euo pipefail

# Run evaluation for a single agent.
# Usage: ./scripts/eval-single.sh <category> <agent_name>
# Example: ./scripts/eval-single.sh hr_people_ops employee_directory

if [ $# -lt 2 ]; then
  echo "Usage: $0 <category> <agent_name>"
  echo "Example: $0 hr_people_ops employee_directory"
  echo ""
  echo "Categories: hr_people_ops, it_service_mgmt, finance_procurement,"
  echo "            customer_sales, supply_chain, compliance_risk"
  exit 1
fi

CATEGORY="$1"
AGENT_NAME="$2"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
AGENT_DIR="$PROJECT_ROOT/agents/$CATEGORY/$AGENT_NAME"
ENV_FILE="${ENV_FILE:-$PROJECT_ROOT/.env}"

if [ ! -d "$AGENT_DIR" ]; then
  echo "ERROR: Agent directory not found: $AGENT_DIR"
  exit 1
fi

TEST_CASES_DIR="$AGENT_DIR/test_cases"
if [ ! -d "$TEST_CASES_DIR" ] || [ -z "$(ls -A "$TEST_CASES_DIR" 2>/dev/null)" ]; then
  echo "ERROR: No test cases found in $TEST_CASES_DIR"
  exit 1
fi

OUTPUT_DIR="$PROJECT_ROOT/eval/output/$CATEGORY/$AGENT_NAME"
mkdir -p "$OUTPUT_DIR"

echo "=== Evaluating: $CATEGORY/$AGENT_NAME ==="
orchestrate evaluations evaluate \
  -p "$TEST_CASES_DIR" \
  -o "$OUTPUT_DIR" \
  -e "$ENV_FILE"

echo ""
echo "Results saved to: $OUTPUT_DIR"
