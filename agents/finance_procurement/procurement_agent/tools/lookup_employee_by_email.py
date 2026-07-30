from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "ops.lead@company.com": {
        "employee_id": "OPS-LEAD-001",
        "name": "Ops Lead",
        "role": "Operations Lead",
        "department": "Operations",
    },
    "eng.manager@company.com": {
        "employee_id": "ENG-MGR-001",
        "name": "Engineering Manager",
        "role": "Engineering Manager",
        "department": "Engineering",
    },
    "pm@company.com": {
        "employee_id": "PM-001",
        "name": "Project Manager",
        "role": "Project Manager",
        "department": "Product Management",
    },
    "admin@company.com": {
        "employee_id": "ADMIN-001",
        "name": "Admin User",
        "role": "IT Administrator",
        "department": "IT",
    },
}


@tool()
def lookup_employee_by_email(email: str):
    """
    Looks up an employee's information by their email address.

    Args:
        email: The employee's email address (e.g. "ops.lead@company.com").

    Returns:
        Employee details including employee_id, name, role, and department, or None if not found.
    """
    normalized = str(email).lower().strip()
    return STUB_RESPONSES.get(normalized)
