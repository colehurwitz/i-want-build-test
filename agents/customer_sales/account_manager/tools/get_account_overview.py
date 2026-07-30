from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "a-100": {
        "account_id": "A-100",
        "name": "Pinnacle Corp",
        "tier": "enterprise",
        "arr": 250000.00,
        "health_score": 82,
        "nps_score": 8,
        "primary_contact": "Sarah VP",
        "csm": "Jane Smith",
        "active_users": 150,
        "last_review_date": "2024-01-15",
        "status": "active",
    },
    "a-200": {
        "account_id": "A-200",
        "name": "Nexus Industries",
        "tier": "enterprise",
        "arr": 180000.00,
        "health_score": 45,
        "nps_score": 4,
        "primary_contact": "Mike Director",
        "csm": "Jane Smith",
        "active_users": 80,
        "last_review_date": "2023-11-20",
        "status": "at_risk",
    },
    "a-300": {
        "account_id": "A-300",
        "name": "Vertex Solutions",
        "tier": "mid_market",
        "arr": 75000.00,
        "health_score": 58,
        "nps_score": 5,
        "primary_contact": "Tom Manager",
        "csm": "Bob Johnson",
        "active_users": 35,
        "last_review_date": "2024-02-01",
        "status": "active",
    },
    "a-400": {
        "account_id": "A-400",
        "name": "Summit Tech",
        "tier": "enterprise",
        "arr": 320000.00,
        "health_score": 91,
        "nps_score": 9,
        "primary_contact": "Lisa CTO",
        "csm": "Jane Smith",
        "active_users": 220,
        "last_review_date": "2024-03-01",
        "status": "active",
    },
    "a-500": {
        "account_id": "A-500",
        "name": "Horizon Digital",
        "tier": "enterprise",
        "arr": 150000.00,
        "health_score": 76,
        "nps_score": 7,
        "primary_contact": "Alex CEO",
        "csm": "Bob Johnson",
        "active_users": 95,
        "last_review_date": "2024-02-15",
        "status": "active",
    },
}


@tool()
def get_account_overview(account_id: str):
    """
    Retrieves a high-level overview of a customer account.

    Args:
        account_id: The unique account identifier (e.g. "A-100").

    Returns:
        Account overview including tier, ARR, health score, NPS, active users, and status, or None if not found.
    """
    normalized = str(account_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
