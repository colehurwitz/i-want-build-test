from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "a-100": {
        "account_id": "A-100",
        "competitor_activity": False,
        "competitors_detected": [],
        "risk_level": "low",
        "last_checked": "2024-03-10",
        "notes": "No competitive activity detected",
    },
    "a-200": {
        "account_id": "A-200",
        "competitor_activity": True,
        "competitors_detected": [
            {"name": "CompetitorX", "product": "Enterprise Suite", "stage": "evaluation", "first_detected": "2024-02-15"},
        ],
        "risk_level": "high",
        "last_checked": "2024-03-12",
        "notes": "Account champion mentioned evaluating CompetitorX during last call",
    },
    "a-300": {
        "account_id": "A-300",
        "competitor_activity": True,
        "competitors_detected": [
            {"name": "RivalCo", "product": "Analytics Platform", "stage": "demo_scheduled", "first_detected": "2024-03-01"},
        ],
        "risk_level": "medium",
        "last_checked": "2024-03-14",
        "notes": "Heard through channel partner that RivalCo is pitching analytics",
    },
    "a-400": {
        "account_id": "A-400",
        "competitor_activity": False,
        "competitors_detected": [],
        "risk_level": "low",
        "last_checked": "2024-03-13",
        "notes": "Strong relationship, no competitive threats identified",
    },
    "a-500": {
        "account_id": "A-500",
        "competitor_activity": False,
        "competitors_detected": [],
        "risk_level": "low",
        "last_checked": "2024-03-11",
        "notes": "Account growing steadily, no competitor interest detected",
    },
}


@tool()
def get_competitive_intel(account_id: str):
    """
    Retrieves competitive intelligence for an account including detected competitor activity.

    Args:
        account_id: The unique account identifier (e.g. "A-100").

    Returns:
        Competitive intel including competitor activity flag, detected competitors, risk level, and notes, or None if not found.
    """
    normalized = str(account_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
