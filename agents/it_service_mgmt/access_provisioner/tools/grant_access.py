from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("adm-001", "usr-200", "database_prod", "read"): {
        "status": "granted",
        "grant_id": "GR-1001",
        "resource": "database_prod",
        "access_level": "read",
        "effective_date": "2024-07-29",
    },
    ("adm-001", "usr-200", "database_prod", "admin"): {
        "status": "granted",
        "grant_id": "GR-1002",
        "resource": "database_prod",
        "access_level": "admin",
        "effective_date": "2024-07-29",
    },
    ("adm-001", "usr-200", "api_gateway", "write"): {
        "status": "granted",
        "grant_id": "GR-1003",
        "resource": "api_gateway",
        "access_level": "write",
        "effective_date": "2024-07-29",
    },
    ("usr-100", "usr-100", "all_systems", "admin"): {
        "status": "granted",
        "grant_id": "GR-1004",
        "resource": "all_systems",
        "access_level": "admin",
        "effective_date": "2024-07-29",
    },
    ("adm-001", "adm-001", "control_panel", "admin"): {
        "status": "warning",
        "grant_id": "GR-1005",
        "message": "Self-modification detected. This action may lock you out.",
    },
}


@tool()
def grant_access(admin_user_id: str, target_user_id: str, resource: str, access_level: str):
    """
    Grants a user access to a resource. Requires admin privileges.

    Args:
        admin_user_id: The admin user's ID performing the grant.
        target_user_id: The target user's ID to receive access.
        resource: The resource name to grant access to.
        access_level: The access level to grant (e.g. "read", "write", "admin").

    Returns:
        Grant result including status, grant_id, and effective date, or None if the operation failed.
    """
    key = (
        str(admin_user_id).lower().strip(),
        str(target_user_id).lower().strip(),
        str(resource).lower().strip(),
        str(access_level).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
