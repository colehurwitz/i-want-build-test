#!/usr/bin/env bash
set -euo pipefail

# Import all agents and their tools into the local Orchestrate environment.
# Activates the local env first, then iterates through all agent directories.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
AGENTS_DIR="$PROJECT_ROOT/agents"

FAILED=()
SUCCEEDED=()

echo "=== Activating local environment ==="
orchestrate env activate local

DOMAINS=(
  hr_people_ops
  it_service_mgmt
  finance_procurement
  customer_sales
  supply_chain
  compliance_risk
)

for domain in "${DOMAINS[@]}"; do
  domain_dir="$AGENTS_DIR/$domain"
  if [ ! -d "$domain_dir" ]; then
    echo "WARN: Domain directory not found: $domain"
    continue
  fi

  for agent_dir in "$domain_dir"/*/; do
    [ ! -d "$agent_dir" ] && continue
    agent_name="$(basename "$agent_dir")"

    echo ""
    echo "--- Importing agent: $domain/$agent_name ---"

    # Import tools first
    for tool_file in "$agent_dir"/tools/*.py; do
      [ ! -f "$tool_file" ] && continue
      echo "  Importing tools from $(basename "$tool_file")..."
      if ! orchestrate tools import -k python -f "$tool_file"; then
        echo "  ERROR: Failed to import tools from $tool_file"
        FAILED+=("$domain/$agent_name (tools: $(basename "$tool_file"))")
        continue 2
      fi
    done

    # Import agent YAML
    agent_yaml=""
    if [ -f "$agent_dir/agent/template.yaml" ]; then
      agent_yaml="$agent_dir/agent/template.yaml"
    elif [ -f "$agent_dir/agent/agent.yaml" ]; then
      agent_yaml="$agent_dir/agent/agent.yaml"
    fi

    if [ -n "$agent_yaml" ]; then
      echo "  Importing agent spec from $(basename "$agent_yaml")..."
      if ! orchestrate agents import -f "$agent_yaml"; then
        echo "  ERROR: Failed to import agent from $agent_yaml"
        FAILED+=("$domain/$agent_name (agent yaml)")
        continue
      fi
    else
      echo "  WARN: No agent YAML found in $agent_dir/agent/"
      FAILED+=("$domain/$agent_name (no agent yaml)")
      continue
    fi

    SUCCEEDED+=("$domain/$agent_name")
  done
done

echo ""
echo "=== Import Summary ==="
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
  exit 1
fi

echo ""
echo "All agents imported successfully."
