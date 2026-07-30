from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "engineering": {
        "department": "Engineering",
        "total_budget": 2000000.00,
        "allocated": 1850000.00,
        "spent": 1200000.00,
        "remaining": 800000.00,
        "fiscal_year": "FY2024",
        "budget_utilization_pct": 60.0,
    },
    "marketing": {
        "department": "Marketing",
        "total_budget": 1500000.00,
        "allocated": 1500000.00,
        "spent": 1450000.00,
        "remaining": 50000.00,
        "fiscal_year": "FY2024",
        "budget_utilization_pct": 96.7,
    },
    "sales": {
        "department": "Sales",
        "total_budget": 1800000.00,
        "allocated": 1600000.00,
        "spent": 900000.00,
        "remaining": 900000.00,
        "fiscal_year": "FY2024",
        "budget_utilization_pct": 50.0,
    },
}


@tool()
def get_department_budget(department: str):
    """
    Retrieves the current budget status for a department.

    Args:
        department: The department name (e.g. "Engineering", "Marketing", "Sales").

    Returns:
        Budget details including total_budget, allocated, spent, remaining, fiscal_year, and utilization percentage, or None if department not found.
    """
    normalized = str(department).lower().strip()
    return STUB_RESPONSES.get(normalized)
