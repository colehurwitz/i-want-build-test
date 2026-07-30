#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== Importing security_incident_responder tools ==="
for tool_file in "$SCRIPT_DIR"/tools/*.py; do
  echo "  Importing $(basename "$tool_file")..."
  orchestrate tools import -k python -f "$tool_file"
done

echo "=== Importing security_incident_responder agent ==="
orchestrate agents import -f "$SCRIPT_DIR/agent/template.yaml"

echo "=== security_incident_responder import complete ==="
