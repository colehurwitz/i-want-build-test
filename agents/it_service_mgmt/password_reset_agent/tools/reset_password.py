from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "u-100": {
        "status": "success",
        "user_id": "U-100",
        "temp_password": "TempPass!2024a",
        "expiry_hours": 24,
        "message": "Password has been reset. User must change password on next login.",
    },
    "u-200": {
        "status": "success",
        "user_id": "U-200",
        "temp_password": "TempPass!2024b",
        "expiry_hours": 24,
        "message": "Password has been reset. User must change password on next login.",
    },
    "u-300": {
        "status": "failed",
        "user_id": "U-300",
        "error": "Account is locked. Cannot reset password until account is unlocked by an administrator.",
    },
    "u-400": {
        "status": "success",
        "user_id": "U-400",
        "temp_password": "TempPass!2024d",
        "expiry_hours": 24,
        "message": "Password has been reset. User must change password on next login.",
    },
    "u-500": {
        "status": "failed",
        "user_id": "U-500",
        "error": "Account is disabled. Cannot reset password for disabled accounts.",
    },
}


@tool()
def reset_password(user_id: str, temp_password: str):
    """
    Resets a user's password to a temporary password.

    Args:
        user_id: The user's ID (e.g. "U-100").
        temp_password: The temporary password to set.

    Returns:
        Reset result including status, temporary password details, and expiry, or None if user not found.
    """
    normalized = str(user_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
