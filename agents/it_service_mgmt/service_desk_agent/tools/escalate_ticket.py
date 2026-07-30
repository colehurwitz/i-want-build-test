from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("tk-5003", "infrastructure"): {
        "status": "escalated",
        "ticket_id": "TK-5003",
        "new_assignee": "Infrastructure Team Lead",
        "escalation_level": "tier_2",
        "response_sla_hours": 2,
    },
    ("tk-5004", "application_support"): {
        "status": "escalated",
        "ticket_id": "TK-5004",
        "new_assignee": "Senior Application Engineer",
        "escalation_level": "tier_2",
        "response_sla_hours": 2,
    },
    ("tk-5002", "network_ops"): {
        "status": "escalated",
        "ticket_id": "TK-5002",
        "new_assignee": "Network Operations Lead",
        "escalation_level": "tier_2",
        "response_sla_hours": 2,
    },
    ("tk-5001", "application_support"): {
        "status": "escalated",
        "ticket_id": "TK-5001",
        "new_assignee": "Senior Application Engineer",
        "escalation_level": "tier_2",
        "response_sla_hours": 1,
    },
}


@tool()
def escalate_ticket(ticket_id: str, reason: str, target_team: str):
    """
    Escalates a support ticket to a higher-level team.

    Args:
        ticket_id: The ticket ID to escalate (e.g. "TK-5003").
        reason: The reason for escalation.
        target_team: The team to escalate to (e.g. "infrastructure", "application_support", "network_ops").

    Returns:
        Escalation result including new assignee, escalation level, and response SLA, or None if escalation failed.
    """
    key = (
        str(ticket_id).lower().strip(),
        str(target_team).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
