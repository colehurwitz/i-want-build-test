from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("adm-001", "usr-200", "database_prod"): {
        "status": "revoked",
        "revoke_id": "RV-1001",
        "resource": "database_prod",
        "effective_date": "2024-07-29",
    },
    ("adm-001", "adm-001", "control_panel"): {
        "status": "warning",
        "revoke_id": "RV-1002",
        "message": "Self-revocation of admin access detected. You may lose control panel access.",
    },
    ("adm-001", "usr-300", "finance_system"): {
        "status": "revoked",
        "revoke_id": "RV-1003",
        "resource": "finance_system",
        "effective_date": "2024-07-29",
    },
}


@tool()
def revoke_access(admin_user_id: str, target_user_id: str, resource: str):
    """
    Revokes a user's access to a resource. Requires admin privileges.

    Args:
        admin_user_id: The admin user's ID performing the revocation.
        target_user_id: The target user's ID to revoke access from.
        resource: The resource name to revoke access to.

    Returns:
        Revocation result including status, revoke_id, and effective date, or None if the operation failed.
    """
    key = (
        str(admin_user_id).lower().strip(),
        str(target_user_id).lower().strip(),
        str(resource).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
