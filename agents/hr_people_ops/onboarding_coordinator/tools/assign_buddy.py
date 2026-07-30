from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("e-500", "engineering"): {
        "employee_id": "E-500",
        "buddy_id": "E-105",
        "buddy_name": "Sarah Kim",
        "department": "Engineering",
        "status": "assigned",
        "buddy_tenure_months": 24,
    },
    ("e-501", "sales"): {
        "employee_id": "E-501",
        "buddy_id": None,
        "buddy_name": None,
        "department": "Sales",
        "status": "no_eligible_buddies",
        "message": "No buddies with 6+ months tenure available in Sales department. Escalate to department manager.",
    },
    ("e-502", "engineering"): {
        "employee_id": "E-502",
        "buddy_id": "E-106",
        "buddy_name": "James Park",
        "department": "Engineering",
        "status": "assigned",
        "buddy_tenure_months": 18,
    },
    ("e-503", "engineering"): {
        "employee_id": "E-503",
        "buddy_id": "E-107",
        "buddy_name": "Chen Wei",
        "department": "Engineering",
        "status": "assigned",
        "buddy_tenure_months": 36,
    },
    ("e-504", "engineering"): {
        "employee_id": "E-504",
        "buddy_id": None,
        "buddy_name": None,
        "department": "Engineering",
        "status": "capacity_exceeded",
        "message": "All eligible buddies in Engineering are at maximum capacity (2 new hires each). Escalate to department manager.",
    },
}


@tool()
def assign_buddy(employee_id: str, department: str):
    """
    Assigns an onboarding buddy to a new employee from the same department.

    Args:
        employee_id: The new employee's ID (e.g. "E-500").
        department: The department to find a buddy in (e.g. "Engineering").

    Returns:
        The buddy assignment result including buddy name and tenure, or a status indicating no eligible buddies are available.
    """
    key = (
        str(employee_id).lower().strip(),
        str(department).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
