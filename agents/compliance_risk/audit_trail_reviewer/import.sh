#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== Importing audit_trail_reviewer tools ==="
for tool_file in "$SCRIPT_DIR"/tools/*.py; do
  echo "  Importing $(basename "$tool_file")..."
  orchestrate tools import -k python -f "$tool_file"
done

echo "=== Importing audit_trail_reviewer agent ==="
orchestrate agents import -f "$SCRIPT_DIR/agent/template.yaml"

echo "=== audit_trail_reviewer import complete ==="
