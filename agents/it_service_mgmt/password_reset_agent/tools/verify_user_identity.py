from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("maria@company.com", "fluffy"): {
        "user_id": "U-100",
        "verified": True,
        "account_status": "active",
        "name": "Maria Garcia",
    },
    ("john@company.com", "blue"): {
        "user_id": "U-200",
        "verified": False,
        "account_status": "active",
        "name": "John Taylor",
    },
    ("john@company.com", "ocean"): {
        "user_id": "U-200",
        "verified": True,
        "account_status": "active",
        "name": "John Taylor",
    },
    ("locked.user@company.com", "correct"): {
        "user_id": "U-300",
        "verified": True,
        "account_status": "locked",
        "name": "Sam Porter",
    },
    ("admin@company.com", "admin123"): {
        "user_id": "U-400",
        "verified": True,
        "account_status": "active",
        "name": "Alex Admin",
    },
    ("disabled@company.com", "mypass"): {
        "user_id": "U-500",
        "verified": True,
        "account_status": "disabled",
        "name": "Dana Reeves",
    },
}


@tool()
def verify_user_identity(email: str, security_answer: str):
    """
    Verifies a user's identity using their email and security question answer.

    Args:
        email: The user's email address.
        security_answer: The user's answer to their security question.

    Returns:
        Verification result including user_id, verified status, and account_status, or None if user not found.
    """
    key = (
        str(email).lower().strip(),
        str(security_answer).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
