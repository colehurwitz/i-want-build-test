from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "john@company.com": {
        "employee_id": "EMP-100",
        "name": "John Miller",
        "department": "Engineering",
        "manager_id": "EMP-500",
        "spending_limit": 5000.00,
    },
    "alice@company.com": {
        "employee_id": "EMP-101",
        "name": "Alice Park",
        "department": "Marketing",
        "manager_id": "EMP-501",
        "spending_limit": 3000.00,
    },
    "bob@company.com": {
        "employee_id": "EMP-102",
        "name": "Bob Torres",
        "department": "Sales",
        "manager_id": "EMP-502",
        "spending_limit": 4000.00,
    },
    "dev@company.com": {
        "employee_id": "EMP-103",
        "name": "Dev Patel",
        "department": "Engineering",
        "manager_id": "EMP-500",
        "spending_limit": 5000.00,
    },
    "manager@company.com": {
        "employee_id": "EMP-500",
        "name": "Karen Wu",
        "department": "Engineering",
        "manager_id": "EMP-900",
        "spending_limit": 10000.00,
    },
}


@tool()
def get_employee_id(email: str):
    """
    Looks up an employee by their email address.

    Args:
        email: The employee's email address (e.g. "john@company.com").

    Returns:
        Employee details including employee_id, name, department, manager_id, and spending_limit, or None if not found.
    """
    normalized = str(email).lower().strip()
    return STUB_RESPONSES.get(normalized)
