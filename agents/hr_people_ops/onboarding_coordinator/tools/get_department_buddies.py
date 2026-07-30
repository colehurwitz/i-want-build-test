from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "engineering": [
        {
            "employee_id": "E-105",
            "name": "Sarah Kim",
            "tenure_months": 24,
            "current_buddy_count": 0,
            "max_buddy_capacity": 2,
            "eligible": True,
        },
        {
            "employee_id": "E-106",
            "name": "James Park",
            "tenure_months": 18,
            "current_buddy_count": 1,
            "max_buddy_capacity": 2,
            "eligible": True,
        },
        {
            "employee_id": "E-107",
            "name": "Chen Wei",
            "tenure_months": 36,
            "current_buddy_count": 2,
            "max_buddy_capacity": 2,
            "eligible": False,
        },
    ],
    "sales": [
        {
            "employee_id": "E-205",
            "name": "Tom Rivera",
            "tenure_months": 4,
            "current_buddy_count": 0,
            "max_buddy_capacity": 2,
            "eligible": False,
        },
    ],
    "hr": [
        {
            "employee_id": "E-305",
            "name": "Maria Garcia",
            "tenure_months": 12,
            "current_buddy_count": 0,
            "max_buddy_capacity": 2,
            "eligible": True,
        },
    ],
}


@tool()
def get_department_buddies(department: str):
    """
    Gets the list of potential onboarding buddies in a department with their eligibility status.

    Args:
        department: The department name (e.g. "Engineering", "Sales").

    Returns:
        A list of potential buddies with their tenure, current buddy count, capacity, and eligibility status, or None if the department is not found.
    """
    normalized = str(department).lower().strip()
    return STUB_RESPONSES.get(normalized)
