#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== Importing password_reset_agent tools ==="
for tool_file in "$SCRIPT_DIR"/tools/*.py; do
  echo "  Importing $(basename "$tool_file")..."
  orchestrate tools import -k python -f "$tool_file"
done

echo "=== Importing password_reset_agent agent ==="
orchestrate agents import -f "$SCRIPT_DIR/agent/template.yaml"

echo "=== password_reset_agent import complete ==="
