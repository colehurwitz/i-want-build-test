from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "engineering": {
        "total_budget": 500000.00,
        "spent_ytd": 420000.00,
        "remaining": 80000.00,
        "warning_threshold": 0.90,
        "budget_status": "on_track",
    },
    "marketing": {
        "total_budget": 300000.00,
        "spent_ytd": 295000.00,
        "remaining": 5000.00,
        "warning_threshold": 0.90,
        "budget_status": "over_threshold",
    },
    "sales": {
        "total_budget": 400000.00,
        "spent_ytd": 250000.00,
        "remaining": 150000.00,
        "warning_threshold": 0.90,
        "budget_status": "on_track",
    },
}


@tool()
def check_department_budget(department: str):
    """
    Checks the remaining budget for a department.

    Args:
        department: The department name (e.g. "Engineering", "Marketing", "Sales").

    Returns:
        Budget details including total_budget, spent_ytd, remaining amount, and budget_status, or None if department not found.
    """
    normalized = str(department).lower().strip()
    return STUB_RESPONSES.get(normalized)
