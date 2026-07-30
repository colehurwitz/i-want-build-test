from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("usr-vip-001", "software", "high"): {
        "ticket_id": "TK-5001",
        "assigned_team": "application_support",
        "sla_hours": 4,
        "priority": "high",
        "status": "open",
    },
    ("usr-vip-001", "software", "critical"): {
        "ticket_id": "TK-5001",
        "assigned_team": "application_support",
        "sla_hours": 1,
        "priority": "critical",
        "status": "open",
    },
    ("usr-dev-100", "network", "medium"): {
        "ticket_id": "TK-5002",
        "assigned_team": "network_ops",
        "sla_hours": 8,
        "priority": "medium",
        "status": "open",
    },
    ("usr-dev-100", "network", "high"): {
        "ticket_id": "TK-5002",
        "assigned_team": "network_ops",
        "sla_hours": 4,
        "priority": "high",
        "status": "open",
    },
    ("usr-std-200", "hardware", "medium"): {
        "ticket_id": "TK-5003",
        "assigned_team": "infrastructure",
        "sla_hours": 8,
        "priority": "medium",
        "status": "open",
    },
    ("usr-mgr-300", "software", "critical"): {
        "ticket_id": "TK-5004",
        "assigned_team": "application_support",
        "sla_hours": 1,
        "priority": "critical",
        "status": "open",
    },
    ("usr-new-400", "access", "low"): {
        "ticket_id": "TK-5005",
        "assigned_team": "identity_access",
        "sla_hours": 24,
        "priority": "low",
        "status": "open",
    },
    ("usr-dev-100", "software", "medium"): {
        "ticket_id": "TK-5006",
        "assigned_team": "application_support",
        "sla_hours": 8,
        "priority": "medium",
        "status": "open",
    },
}


@tool()
def create_ticket(user_id: str, category: str, priority: str, description: str):
    """
    Creates a support ticket for tracking and resolution.

    Args:
        user_id: The requesting user's ID (e.g. "USR-VIP-001").
        category: The ticket category ("hardware", "software", "network", "access", "other").
        priority: The ticket priority ("critical", "high", "medium", "low").
        description: Detailed description of the issue including symptoms and diagnostic results.

    Returns:
        Ticket details including ticket_id, assigned_team, SLA hours, and status, or None if creation failed.
    """
    key = (
        str(user_id).lower().strip(),
        str(category).lower().strip(),
        str(priority).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
