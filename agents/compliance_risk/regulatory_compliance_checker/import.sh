#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== Importing regulatory_compliance_checker tools ==="
for tool_file in "$SCRIPT_DIR"/tools/*.py; do
  echo "  Importing $(basename "$tool_file")..."
  orchestrate tools import -k python -f "$tool_file"
done

echo "=== Importing regulatory_compliance_checker agent ==="
orchestrate agents import -f "$SCRIPT_DIR/agent/template.yaml"

echo "=== regulatory_compliance_checker import complete ==="
