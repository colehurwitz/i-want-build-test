from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "m-100": {
        "manager_id": "M-100",
        "manager_name": "David Lee",
        "department": "Engineering",
        "direct_reports": [
            {
                "employee_id": "E-100",
                "name": "John Smith",
                "title": "Software Engineer",
            },
            {
                "employee_id": "E-101",
                "name": "Jane Doe",
                "title": "Senior Engineer",
            },
        ],
    },
    "m-200": {
        "manager_id": "M-200",
        "manager_name": "Lisa Chen",
        "department": "Sales",
        "direct_reports": [
            {
                "employee_id": "E-200",
                "name": "Sarah Wilson",
                "title": "Account Executive",
            },
            {
                "employee_id": "E-201",
                "name": "Mike Brown",
                "title": "Sales Representative",
            },
        ],
    },
}


@tool()
def get_org_chart(manager_id: str):
    """
    Gets the organizational chart for a manager showing their direct reports.

    Args:
        manager_id: The manager's employee ID (e.g. "M-100").

    Returns:
        The manager's info and list of direct reports, or None if the manager is not found.
    """
    normalized = str(manager_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
