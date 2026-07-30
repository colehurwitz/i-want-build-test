from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("payments", "critical"): {
        "notified": True,
        "oncall_person": "Pat Rivera",
        "team": "payments",
        "escalation_triggered": True,
        "response_expected_minutes": 5,
    },
    ("payments", "high"): {
        "notified": True,
        "oncall_person": "Pat Rivera",
        "team": "payments",
        "escalation_triggered": False,
        "response_expected_minutes": 15,
    },
    ("auth", "critical"): {
        "notified": True,
        "oncall_person": "Jordan Kim",
        "team": "auth",
        "escalation_triggered": True,
        "response_expected_minutes": 5,
    },
    ("auth", "high"): {
        "notified": True,
        "oncall_person": "Jordan Kim",
        "team": "auth",
        "escalation_triggered": False,
        "response_expected_minutes": 15,
    },
    ("frontend", "low"): {
        "notified": True,
        "oncall_person": "Taylor Brooks",
        "team": "frontend",
        "escalation_triggered": False,
        "response_expected_minutes": 60,
    },
    ("frontend", "critical"): {
        "notified": True,
        "oncall_person": "Taylor Brooks",
        "team": "frontend",
        "escalation_triggered": True,
        "response_expected_minutes": 5,
    },
}


@tool()
def notify_oncall(team: str, severity: str, message: str):
    """
    Notifies the on-call person for a team about an incident.

    Args:
        team: The team to notify (e.g. "payments", "auth", "frontend").
        severity: The incident severity ("critical", "high", "medium", "low").
        message: The notification message with incident details.

    Returns:
        Notification result including oncall person, escalation status, and expected response time, or None if team not found.
    """
    key = (
        str(team).lower().strip(),
        str(severity).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
