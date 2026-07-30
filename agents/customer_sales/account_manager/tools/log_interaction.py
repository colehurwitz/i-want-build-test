from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("a-100", "review"): {
        "interaction_id": "INT-4001",
        "account_id": "A-100",
        "interaction_type": "review",
        "status": "logged",
        "logged_at": "2024-03-15T16:00:00Z",
    },
    ("a-200", "review"): {
        "interaction_id": "INT-4002",
        "account_id": "A-200",
        "interaction_type": "review",
        "status": "logged",
        "logged_at": "2024-03-15T16:30:00Z",
    },
    ("a-200", "escalation"): {
        "interaction_id": "INT-4003",
        "account_id": "A-200",
        "interaction_type": "escalation",
        "status": "logged",
        "logged_at": "2024-03-15T17:00:00Z",
    },
    ("a-300", "review"): {
        "interaction_id": "INT-4004",
        "account_id": "A-300",
        "interaction_type": "review",
        "status": "logged",
        "logged_at": "2024-03-15T17:30:00Z",
    },
    ("a-400", "review"): {
        "interaction_id": "INT-4005",
        "account_id": "A-400",
        "interaction_type": "review",
        "status": "logged",
        "logged_at": "2024-03-15T18:00:00Z",
    },
    ("a-500", "review"): {
        "interaction_id": "INT-4006",
        "account_id": "A-500",
        "interaction_type": "review",
        "status": "logged",
        "logged_at": "2024-03-15T18:30:00Z",
    },
    ("a-500", "call"): {
        "interaction_id": "INT-4007",
        "account_id": "A-500",
        "interaction_type": "call",
        "status": "logged",
        "logged_at": "2024-03-15T19:00:00Z",
    },
}


@tool()
def log_interaction(account_id: str, interaction_type: str, summary: str, follow_up_date: str):
    """
    Logs a customer interaction for an account.

    Args:
        account_id: The unique account identifier (e.g. "A-100").
        interaction_type: The type of interaction ("meeting", "call", "email", "escalation", "review").
        summary: A summary of the interaction and key discussion points.
        follow_up_date: The date for the next follow-up action (e.g. "2024-04-15").

    Returns:
        Interaction log confirmation including interaction_id and status, or None if logging failed.
    """
    key = (
        str(account_id).lower().strip(),
        str(interaction_type).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
