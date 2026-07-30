from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "admin@company.com": {
        "user_id": "ADM-001",
        "role": "admin",
        "department": "IT",
        "name": "Alice Admin",
    },
    "admin2@company.com": {
        "user_id": "ADM-002",
        "role": "admin",
        "department": "IT",
        "name": "Bob Admin",
    },
    "regular.user@company.com": {
        "user_id": "USR-100",
        "role": "user",
        "department": "Marketing",
        "name": "Carol User",
    },
    "bob@company.com": {
        "user_id": "USR-200",
        "role": "user",
        "department": "Engineering",
        "name": "Bob Developer",
    },
    "viewer@company.com": {
        "user_id": "USR-300",
        "role": "viewer",
        "department": "Finance",
        "name": "Diana Viewer",
    },
    "intern@company.com": {
        "user_id": "USR-400",
        "role": "viewer",
        "department": "Engineering",
        "name": "Evan Intern",
    },
}


@tool()
def get_user_role(email: str):
    """
    Looks up a user's role and department by their email address.

    Args:
        email: The user's email address.

    Returns:
        User details including user_id, role (admin/user/viewer), department, and name, or None if not found.
    """
    normalized = str(email).lower().strip()
    return STUB_RESPONSES.get(normalized)
