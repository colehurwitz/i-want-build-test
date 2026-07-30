from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "usr-200": [
        {"resource": "database_prod", "access_level": "read", "granted_date": "2024-03-15"},
        {"resource": "code_repo", "access_level": "write", "granted_date": "2024-01-10"},
        {"resource": "staging_env", "access_level": "admin", "granted_date": "2024-02-20"},
    ],
    "usr-100": [
        {"resource": "marketing_tools", "access_level": "write", "granted_date": "2024-04-01"},
        {"resource": "analytics_dashboard", "access_level": "read", "granted_date": "2024-05-15"},
    ],
    "adm-001": [
        {"resource": "control_panel", "access_level": "admin", "granted_date": "2024-01-01"},
        {"resource": "database_prod", "access_level": "admin", "granted_date": "2024-01-01"},
        {"resource": "all_systems", "access_level": "admin", "granted_date": "2024-01-01"},
    ],
    "usr-300": [
        {"resource": "finance_system", "access_level": "read", "granted_date": "2024-06-01"},
        {"resource": "reporting_dashboard", "access_level": "read", "granted_date": "2024-06-01"},
    ],
    "usr-400": [
        {"resource": "code_repo", "access_level": "read", "granted_date": "2024-07-01"},
    ],
}


@tool()
def list_user_permissions(user_id: str):
    """
    Lists all permissions currently assigned to a user.

    Args:
        user_id: The user's ID (e.g. "USR-200").

    Returns:
        A list of permission records with resource, access_level, and granted_date, or None if user not found.
    """
    normalized = str(user_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
