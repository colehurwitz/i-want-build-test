from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "engineering": [
        {
            "employee_id": "E-100",
            "name": "John Smith",
            "title": "Software Engineer",
            "email": "john.smith@company.com",
        },
        {
            "employee_id": "E-101",
            "name": "Jane Doe",
            "title": "Senior Engineer",
            "email": "jane.doe@company.com",
        },
        {
            "employee_id": "M-100",
            "name": "David Lee",
            "title": "VP Engineering",
            "email": "david.lee@company.com",
        },
    ],
    "sales": [
        {
            "employee_id": "E-200",
            "name": "Sarah Wilson",
            "title": "Account Executive",
            "email": "sarah.wilson@company.com",
        },
        {
            "employee_id": "E-201",
            "name": "Mike Brown",
            "title": "Sales Representative",
            "email": "mike.brown@company.com",
        },
        {
            "employee_id": "M-200",
            "name": "Lisa Chen",
            "title": "VP Sales",
            "email": "lisa.chen@company.com",
        },
    ],
}


@tool()
def get_department_roster(department: str):
    """
    Gets the full roster of employees in a department.

    Args:
        department: The department name (e.g. "Engineering", "Sales").

    Returns:
        A list of employees in the department with their IDs, names, titles, and emails, or None if the department is not found.
    """
    normalized = str(department).lower().strip()
    return STUB_RESPONSES.get(normalized)
