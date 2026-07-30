from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("u-500", 30): {
        "user_id": "U-500",
        "period_days": 30,
        "total_actions": 342,
        "login_locations": ["185.220.101.42 (TOR)", "10.0.1.60 (office)", "192.168.1.100 (VPN)"],
        "role_changes": [
            {"date": "2024-07-23", "from": "user", "to": "admin", "approved_by": "self"},
        ],
        "unusual_patterns": [
            "3 logins from TOR exit nodes in 30 days",
            "Self-approved privilege escalation on 2024-07-23",
            "Access to 12 restricted resources after escalation",
        ],
        "risk_assessment": "HIGH — multiple indicators of compromised account or insider threat",
    },
    ("u-500", 7): {
        "user_id": "U-500",
        "period_days": 7,
        "total_actions": 89,
        "login_locations": ["185.220.101.42 (TOR)", "10.0.1.60 (office)"],
        "role_changes": [
            {"date": "2024-07-23", "from": "user", "to": "admin", "approved_by": "self"},
        ],
        "unusual_patterns": [
            "TOR-based login followed by immediate privilege escalation",
            "Accessed 8 restricted resources in 2 hours after escalation",
        ],
        "risk_assessment": "HIGH — strong indicators of account compromise",
    },
    ("u-302", 30): {
        "user_id": "U-302",
        "period_days": 30,
        "total_actions": 456,
        "login_locations": ["10.0.1.55 (office)"],
        "role_changes": [],
        "unusual_patterns": [
            "After-hours bulk export on 2024-07-25 (2:30 AM, 5000 records)",
            "Normal activity pattern otherwise (9 AM - 6 PM)",
        ],
        "risk_assessment": "MEDIUM — single after-hours bulk export warrants investigation",
    },
    ("u-401", 30): {
        "user_id": "U-401",
        "period_days": 30,
        "total_actions": 278,
        "login_locations": ["10.0.2.20 (office)"],
        "role_changes": [],
        "unusual_patterns": [
            "Daily refund processing pattern — 3 consecutive days",
            "All refunds processed to same merchant account",
        ],
        "risk_assessment": "MEDIUM — refund pattern may indicate fraud or policy violation",
    },
}


@tool()
def get_user_activity(user_id: str, days: int):
    """
    Retrieves a user's activity summary for a specified number of past days.

    Args:
        user_id: The user identifier (e.g. "U-500").
        days: The number of days of activity to retrieve (e.g. 7, 30).

    Returns:
        User activity summary including total actions, login locations, role changes, unusual patterns, and risk assessment, or None if not found.
    """
    key = (str(user_id).lower().strip(), int(days))
    return STUB_RESPONSES.get(key)
