# Agent Test Suite for watsonx Orchestrate ADK Eval & Optimization

A repository of 24 diverse watsonx Orchestrate ADK agents spanning 6 enterprise domains, designed as a benchmark where prompt optimization technology can demonstrate measurable improvement.

Each agent has calibrated instruction quality creating a gradient of optimization difficulty (EASY/MEDIUM/HARD). Tools use the stub-data-dict pattern (STUB_RESPONSES returning dicts/lists directly), and test cases feature complex interdependent goal DAGs (3-6+ steps).

## Directory Structure

```
agents/
├── hr_people_ops/          # 4 agents: employee_directory, leave_manager, payroll_processor, onboarding_coordinator
├── it_service_mgmt/        # 4 agents: password_reset_agent, access_provisioner, incident_commander, service_desk_agent
├── finance_procurement/    # 4 agents: expense_reporter, invoice_processor, budget_analyst, procurement_agent
├── customer_sales/         # 4 agents: lead_qualifier, deal_pipeline, customer_support, account_manager
├── supply_chain/           # 4 agents: inventory_tracker, shipping_coordinator, order_fulfillment, vendor_manager
├── compliance_risk/        # 4 agents: data_privacy_officer, audit_trail_reviewer, security_incident_responder, regulatory_compliance_checker
└── shared/                 # Shared tool utilities
eval/
├── configs/                # Eval configuration templates
└── output/                 # Eval results (gitignored)
scripts/
├── import-all.sh           # Import all agents into Orchestrate
├── eval-all.sh             # Evaluate all agents
├── eval-single.sh          # Evaluate a single agent
└── eval-tier.sh            # Evaluate agents by difficulty tier
```

Each agent directory contains:
- `agent/template.yaml` — Agent spec (kind, style, tools, instructions, model_overrides)
- `tools/*.py` — One file per tool using `@tool` decorator with STUB_RESPONSES
- `test_cases/*.json` — Test cases with goal DAGs, tags, and starting sentences

## Prerequisites

- Python 3.11+
- [watsonx Orchestrate ADK SDK](https://pypi.org/project/ibm-watsonx-orchestrate/) (`ibm_watsonx_orchestrate >= 0.9.2`)
- Docker (for local Developer Edition) or access to a remote Orchestrate instance
- `orchestrate` CLI installed and configured

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your WATSONX_APIKEY and WATSONX_SPACE_ID
   ```

   If you already have a `.env` file elsewhere (e.g., `~/ibm/wxo-clients/.env`), you can symlink it:
   ```bash
   ln -s /path/to/your/.env .env
   ```

3. **Activate local environment:**
   ```bash
   orchestrate env activate local
   ```

## Importing Agents

Import all agents and their tools:
```bash
./scripts/import-all.sh
```

## Running Evaluations

**All agents:**
```bash
./scripts/eval-all.sh
```

**Single agent:**
```bash
./scripts/eval-single.sh <category> <agent_name>
# Example:
./scripts/eval-single.sh hr_people_ops employee_directory
```

**By difficulty tier:**
```bash
./scripts/eval-tier.sh <easy|medium|hard>
# Example:
./scripts/eval-tier.sh easy
```

## Difficulty Gradient

| Tier | Agents | Baseline | Instruction Quality | Optimization Challenge |
|------|--------|----------|--------------------|-----------------------|
| EASY (7) | 1, 5, 6, 9, 13, 17, 18 | ~30-40% | Terrible/minimal | Obvious gaps — missing tool selection, no validation |
| MEDIUM (10) | 2, 3, 7, 10, 11, 14, 15, 19, 21, 22 | ~50-60% | Decent but incomplete | Missing edge cases — no policy checks, no error handling |
| HARD (7) | 4, 8, 12, 16, 20, 23, 24 | ~70-80% | Near-complete | Subtle gaps — one missing validation, one unhandled edge case |

## Agent Styles

All four ADK agent styles are represented equally (6 agents each):
- `default` — Standard tool-calling
- `react_core` — ReAct reasoning with core tools
- `react_intrinsic` — ReAct with intrinsic knowledge
- `planner` — Multi-step planning before execution

## Key Patterns

**Tool pattern (STUB_RESPONSES):**
```python
from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "key1": {"field_a": "value1", "field_b": 42},
}

@tool()
def get_something(param_id: str):
    """Gets something from the system.

    Args:
        param_id: The unique identifier.

    Returns:
        The record details or None if not found.
    """
    normalized = str(param_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
```

**Test case format:**
```json
{
  "tags": ["agent_style:default", "journey_complexity:medium", "tool_type:python_tool",
           "category:hr_people_ops", "test_type:multi_operation_chain", "optimization_difficulty:easy"],
  "agent": "agent_name",
  "goals": {"tool_a-1": ["tool_b-1"], "tool_b-1": []},
  "goal_details": [
    {"args": {"email": "user@example.com"}, "name": "tool_a-1", "type": "tool_call", "tool_name": "tool_a"},
    {"args": {"id": "123"}, "name": "tool_b-1", "type": "tool_call", "tool_name": "tool_b"}
  ],
  "story": "Description of the scenario.",
  "starting_sentence": "What the user says."
}
```
