#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== Importing incident_commander tools ==="
for tool_file in "$SCRIPT_DIR"/tools/*.py; do
  echo "  Importing $(basename "$tool_file")..."
  orchestrate tools import -k python -f "$tool_file"
done

echo "=== Importing incident_commander agent ==="
orchestrate agents import -f "$SCRIPT_DIR/agent/template.yaml"

echo "=== incident_commander import complete ==="
