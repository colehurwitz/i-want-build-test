from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("usr-200", "database_prod"): {
        "has_access": True,
        "access_level": "read",
        "granted_date": "2024-03-15",
        "granted_by": "ADM-001",
    },
    ("usr-200", "api_gateway"): {
        "has_access": False,
        "access_level": None,
        "granted_date": None,
        "granted_by": None,
    },
    ("usr-100", "all_systems"): {
        "has_access": False,
        "access_level": None,
        "granted_date": None,
        "granted_by": None,
    },
    ("adm-001", "control_panel"): {
        "has_access": True,
        "access_level": "admin",
        "granted_date": "2024-01-01",
        "granted_by": "SYSTEM",
    },
    ("usr-300", "finance_system"): {
        "has_access": True,
        "access_level": "read",
        "granted_date": "2024-06-01",
        "granted_by": "ADM-002",
    },
    ("usr-100", "finance_system"): {
        "has_access": False,
        "access_level": None,
        "granted_date": None,
        "granted_by": None,
    },
}


@tool()
def check_permission(user_id: str, resource: str):
    """
    Checks whether a user has access to a specific resource.

    Args:
        user_id: The user's ID (e.g. "USR-200").
        resource: The resource name to check access for (e.g. "database_prod").

    Returns:
        Permission details including has_access, access_level, and grant info, or None if not found.
    """
    key = (
        str(user_id).lower().strip(),
        str(resource).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
