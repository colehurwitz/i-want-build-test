#!/usr/bin/env bash
set -euo pipefail

# Difficulty Verification Workflow
# Runs all 5 phases (B1-B5) to empirically verify EASY/MEDIUM/HARD classifications.
#
# Prerequisites:
#   - WXO Developer Edition server running (orchestrate server start)
#   - Agents imported (./scripts/import-all.sh)
#   - .env file with WATSONX_APIKEY and WATSONX_SPACE_ID

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
RESULTS_DIR="$PROJECT_ROOT/results"
BACKUP_DIR="$RESULTS_DIR/backups"
AGENTS_DIR="$PROJECT_ROOT/agents"
EVAL_OUTPUT="$PROJECT_ROOT/eval/output"
BASELINE_OUTPUT="$RESULTS_DIR/baseline-output"

SAMPLE_AGENTS=(
  "hr_people_ops/employee_directory"
  "hr_people_ops/leave_manager"
  "it_service_mgmt/service_desk_agent"
)

SAMPLE_TIERS=(
  "easy"
  "medium"
  "hard"
)

mkdir -p "$RESULTS_DIR" "$BACKUP_DIR" "$BASELINE_OUTPUT"

echo "========================================="
echo "  DIFFICULTY VERIFICATION WORKFLOW"
echo "========================================="
echo ""

# ---- Phase B1: Environment Setup ----
echo "=== Phase B1: Environment Setup ==="

# Check .env
if [ ! -f "$PROJECT_ROOT/.env" ]; then
  echo "ERROR: No .env file found at $PROJECT_ROOT/.env"
  echo "  Symlink your .env: ln -s ~/wxo-clients/.env $PROJECT_ROOT/.env"
  exit 1
fi

if ! grep -q "WATSONX_APIKEY" "$PROJECT_ROOT/.env"; then
  echo "ERROR: WATSONX_APIKEY not found in .env"
  exit 1
fi

if ! grep -q "WATSONX_SPACE_ID" "$PROJECT_ROOT/.env"; then
  echo "ERROR: WATSONX_SPACE_ID not found in .env"
  exit 1
fi
echo "  ✓ .env file valid"

# Check orchestrate CLI
if ! command -v orchestrate &>/dev/null; then
  echo "ERROR: orchestrate CLI not found. Activate venv: source ~/wxo-clients/.venv-linux/bin/activate"
  exit 1
fi
echo "  ✓ orchestrate CLI available"

# Check eval scripts
for script in eval-single.sh eval-tier.sh; do
  if [ ! -x "$SCRIPT_DIR/$script" ]; then
    echo "ERROR: $script not executable"
    exit 1
  fi
done
echo "  ✓ eval scripts executable"

# Check WXO server
if ! curl -s --connect-timeout 5 http://localhost:4321/health &>/dev/null; then
  echo "ERROR: WXO server not responding at localhost:4321"
  echo "  Start it: orchestrate server start"
  exit 1
fi
echo "  ✓ WXO server running"

# Smoke test
echo ""
echo "  Running smoke test: eval-single.sh hr_people_ops employee_directory"
if ! "$SCRIPT_DIR/eval-single.sh" hr_people_ops employee_directory; then
  echo "ERROR: Smoke test failed"
  exit 1
fi
echo "  ✓ Smoke test passed"
echo ""

# ---- Phase B2: Baseline Evaluation ----
echo "=== Phase B2: Baseline Evaluation ==="

for tier in easy medium hard; do
  echo ""
  echo "  Running tier: $tier"
  "$SCRIPT_DIR/eval-tier.sh" "$tier" || true
done

# Copy baseline results
cp -r "$EVAL_OUTPUT" "$BASELINE_OUTPUT"

# Parse results
echo ""
echo "  Parsing baseline results..."
python3 "$SCRIPT_DIR/parse-eval-results.py" \
  --output-dir "$BASELINE_OUTPUT" \
  --agents-dir "$AGENTS_DIR" > "$RESULTS_DIR/baseline-summary.md"

echo "  ✓ Baseline results saved to results/baseline-summary.md"
echo ""

# ---- Phase B3: Optimize Sample Agents ----
echo "=== Phase B3: Optimize Sample Agents ==="

# Back up originals
for i in "${!SAMPLE_AGENTS[@]}"; do
  agent="${SAMPLE_AGENTS[$i]}"
  agent_name="$(basename "$agent")"
  src="$AGENTS_DIR/$agent/agent/template.yaml"
  cp "$src" "$BACKUP_DIR/${agent_name}_template.yaml.bak"
  echo "  ✓ Backed up $agent_name/template.yaml"
done

# Apply optimizations (already in place via optimized template.yaml files)
echo "  Optimized templates are already in place."

# Re-import optimized agents
for agent in "${SAMPLE_AGENTS[@]}"; do
  agent_name="$(basename "$agent")"
  agent_dir="$AGENTS_DIR/$agent"
  echo "  Re-importing $agent_name..."
  orchestrate agents import -f "$agent_dir/agent/template.yaml" || true
done
echo "  ✓ Optimized agents imported"
echo ""

# ---- Phase B4: Re-evaluate and Measure Deltas ----
echo "=== Phase B4: Re-evaluate Optimized Agents ==="

# Clear eval output for the sample agents
for agent in "${SAMPLE_AGENTS[@]}"; do
  rm -rf "$EVAL_OUTPUT/$agent"
done

# Re-run evals on optimized agents
for i in "${!SAMPLE_AGENTS[@]}"; do
  agent="${SAMPLE_AGENTS[$i]}"
  IFS='/' read -r category agent_name <<< "$agent"
  echo ""
  echo "  Evaluating optimized: $agent"
  "$SCRIPT_DIR/eval-single.sh" "$category" "$agent_name" || true
done

# Generate delta comparison
echo ""
echo "  Computing deltas..."
python3 "$SCRIPT_DIR/parse-eval-results.py" \
  --output-dir "$EVAL_OUTPUT" \
  --agents-dir "$AGENTS_DIR" \
  --baseline-dir "$BASELINE_OUTPUT" > "$RESULTS_DIR/delta-comparison.md"

echo "  ✓ Delta comparison saved to results/delta-comparison.md"
echo ""

# ---- Phase B5: Analyze and Reclassify ----
echo "=== Phase B5: Analyze Results ==="

python3 "$SCRIPT_DIR/analyze-difficulty.py" \
  --baseline-dir "$BASELINE_OUTPUT" \
  --optimized-dir "$EVAL_OUTPUT" \
  --agents-dir "$AGENTS_DIR" \
  --output "$RESULTS_DIR/difficulty-verification-report.md"

echo "  ✓ Report saved to results/difficulty-verification-report.md"

# Restore original templates
echo ""
echo "  Restoring original template.yaml files..."
for i in "${!SAMPLE_AGENTS[@]}"; do
  agent="${SAMPLE_AGENTS[$i]}"
  agent_name="$(basename "$agent")"
  cp "$BACKUP_DIR/${agent_name}_template.yaml.bak" "$AGENTS_DIR/$agent/agent/template.yaml"
  orchestrate agents import -f "$AGENTS_DIR/$agent/agent/template.yaml" || true
  echo "  ✓ Restored $agent_name"
done

echo ""
echo "========================================="
echo "  VERIFICATION COMPLETE"
echo "========================================="
echo ""
echo "Reports:"
echo "  results/baseline-summary.md"
echo "  results/delta-comparison.md"
echo "  results/difficulty-verification-report.md"
