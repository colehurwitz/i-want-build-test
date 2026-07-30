from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "john smith": {
        "employee_id": "E-100",
        "name": "John Smith",
        "email": "john.smith@company.com",
        "department": "Engineering",
        "title": "Software Engineer",
        "phone": "555-0100",
        "manager_id": "M-100",
    },
    "e-100": {
        "employee_id": "E-100",
        "name": "John Smith",
        "email": "john.smith@company.com",
        "department": "Engineering",
        "title": "Software Engineer",
        "phone": "555-0100",
        "manager_id": "M-100",
    },
    "jane doe": {
        "employee_id": "E-101",
        "name": "Jane Doe",
        "email": "jane.doe@company.com",
        "department": "Engineering",
        "title": "Senior Engineer",
        "phone": "555-0101",
        "manager_id": "M-100",
    },
    "e-101": {
        "employee_id": "E-101",
        "name": "Jane Doe",
        "email": "jane.doe@company.com",
        "department": "Engineering",
        "title": "Senior Engineer",
        "phone": "555-0101",
        "manager_id": "M-100",
    },
    "sarah wilson": {
        "employee_id": "E-200",
        "name": "Sarah Wilson",
        "email": "sarah.wilson@company.com",
        "department": "Sales",
        "title": "Account Executive",
        "phone": "555-0200",
        "manager_id": "M-200",
    },
    "e-200": {
        "employee_id": "E-200",
        "name": "Sarah Wilson",
        "email": "sarah.wilson@company.com",
        "department": "Sales",
        "title": "Account Executive",
        "phone": "555-0200",
        "manager_id": "M-200",
    },
    "mike brown": {
        "employee_id": "E-201",
        "name": "Mike Brown",
        "email": "mike.brown@company.com",
        "department": "Sales",
        "title": "Sales Representative",
        "phone": "555-0201",
        "manager_id": "M-200",
    },
    "e-201": {
        "employee_id": "E-201",
        "name": "Mike Brown",
        "email": "mike.brown@company.com",
        "department": "Sales",
        "title": "Sales Representative",
        "phone": "555-0201",
        "manager_id": "M-200",
    },
    "david lee": {
        "employee_id": "M-100",
        "name": "David Lee",
        "email": "david.lee@company.com",
        "department": "Engineering",
        "title": "VP Engineering",
        "phone": "555-0300",
        "manager_id": "M-300",
    },
    "m-100": {
        "employee_id": "M-100",
        "name": "David Lee",
        "email": "david.lee@company.com",
        "department": "Engineering",
        "title": "VP Engineering",
        "phone": "555-0300",
        "manager_id": "M-300",
    },
    "lisa chen": {
        "employee_id": "M-200",
        "name": "Lisa Chen",
        "email": "lisa.chen@company.com",
        "department": "Sales",
        "title": "VP Sales",
        "phone": "555-0301",
        "manager_id": "M-300",
    },
    "m-200": {
        "employee_id": "M-200",
        "name": "Lisa Chen",
        "email": "lisa.chen@company.com",
        "department": "Sales",
        "title": "VP Sales",
        "phone": "555-0301",
        "manager_id": "M-300",
    },
}


@tool()
def lookup_employee(name_or_id: str):
    """
    Looks up an employee by name or employee ID.

    Args:
        name_or_id: The employee's full name or employee ID (e.g. "John Smith" or "E-100").

    Returns:
        The employee's profile including name, email, department, title, phone, and manager ID, or None if not found.
    """
    normalized = str(name_or_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
