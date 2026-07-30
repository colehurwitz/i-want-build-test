from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "u-100": {
        "user_id": "U-100",
        "status": "active",
        "last_login": "2024-07-28T14:30:00Z",
        "failed_attempts": 0,
        "password_expired": False,
        "last_password_change": "2024-06-01",
    },
    "u-200": {
        "user_id": "U-200",
        "status": "active",
        "last_login": "2024-07-25T09:15:00Z",
        "failed_attempts": 2,
        "password_expired": True,
        "last_password_change": "2024-01-15",
    },
    "u-300": {
        "user_id": "U-300",
        "status": "locked",
        "last_login": "2024-07-20T11:00:00Z",
        "failed_attempts": 5,
        "password_expired": False,
        "last_password_change": "2024-05-10",
    },
    "u-400": {
        "user_id": "U-400",
        "status": "active",
        "last_login": "2024-07-29T08:00:00Z",
        "failed_attempts": 0,
        "password_expired": False,
        "last_password_change": "2024-07-01",
    },
    "u-500": {
        "user_id": "U-500",
        "status": "disabled",
        "last_login": "2024-03-15T16:45:00Z",
        "failed_attempts": 0,
        "password_expired": True,
        "last_password_change": "2023-12-01",
    },
}


@tool()
def check_account_status(user_id: str):
    """
    Checks the current status of a user account.

    Args:
        user_id: The user's ID (e.g. "U-100").

    Returns:
        Account status details including status, last login, failed attempts, and password expiry info, or None if not found.
    """
    normalized = str(user_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
