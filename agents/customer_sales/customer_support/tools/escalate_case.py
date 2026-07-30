from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("cs-200", "confirmed bug in api integration", "engineering"): {
        "case_id": "CS-200",
        "escalation_id": "ESC-100",
        "status": "escalated",
        "target_team": "engineering",
        "assigned_to": "Senior Engineer - Alex Chen",
        "priority": "high",
        "escalated_at": "2024-03-15T15:00:00Z",
    },
    ("cs-300", "customer unable to access account after multiple attempts", "tier2"): {
        "case_id": "CS-300",
        "escalation_id": "ESC-101",
        "status": "escalated",
        "target_team": "tier2",
        "assigned_to": "Tier 2 Lead - Maria Santos",
        "priority": "high",
        "escalated_at": "2024-03-15T16:00:00Z",
    },
}


@tool()
def escalate_case(case_id: str, escalation_reason: str, target_team: str):
    """
    Escalates a support case to a specialized team.

    Args:
        case_id: The unique case identifier (e.g. "CS-200").
        escalation_reason: The reason for escalation.
        target_team: The team to escalate to (e.g. "engineering", "tier2", "billing", "security").

    Returns:
        Escalation confirmation including escalation_id, assigned team member, and priority, or None if escalation failed.
    """
    key = (
        str(case_id).lower().strip(),
        str(escalation_reason).lower().strip(),
        str(target_team).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
