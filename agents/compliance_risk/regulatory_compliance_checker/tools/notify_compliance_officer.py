from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("entity-a", "critical"): {
        "entity": "Entity-A",
        "severity": "critical",
        "notification_status": "delivered",
        "recipient": "Chief Compliance Officer",
        "method": "page + email",
        "timestamp": "2024-07-29T10:01:00Z",
        "acknowledgment": "CCO paged and emailed. Response expected within 1 hour.",
        "escalation_note": "Compliance score below 50% — immediate executive review required",
    },
    ("entity-b", "critical"): {
        "entity": "Entity-B",
        "severity": "critical",
        "notification_status": "delivered",
        "recipient": "Chief Compliance Officer + Legal",
        "method": "page + email",
        "timestamp": "2024-07-29T10:06:00Z",
        "acknowledgment": "CCO and Legal paged. ESCALATION: Repeat offender with 4 violations for REG-200.",
        "escalation_note": "Repeat offender status triggered — board notification may be required",
    },
    ("entity-b", "high"): {
        "entity": "Entity-B",
        "severity": "high",
        "notification_status": "delivered",
        "recipient": "Compliance Officer",
        "method": "email",
        "timestamp": "2024-07-29T10:07:00Z",
        "acknowledgment": "Compliance officer notified. Review expected within 24 hours.",
        "escalation_note": "Repeat offender — elevated monitoring recommended",
    },
    ("entity-e", "critical"): {
        "entity": "Entity-E",
        "severity": "critical",
        "notification_status": "delivered",
        "recipient": "Chief Compliance Officer",
        "method": "page + email",
        "timestamp": "2024-07-29T10:21:00Z",
        "acknowledgment": "CCO paged. REG-500 effective date approaching — urgent remediation needed.",
        "escalation_note": "New regulation effective 2024-08-01 — entity unprepared",
    },
}


@tool()
def notify_compliance_officer(entity: str, severity: str, message: str):
    """
    Notifies the compliance officer about compliance findings for an entity.

    Args:
        entity: The business entity name (e.g. "Entity-A").
        severity: The severity of the finding — one of "critical", "high", "medium", or "low".
        message: The notification message describing the compliance findings and recommended actions.

    Returns:
        Notification confirmation including recipient, delivery method, and acknowledgment, or None if notification failed.
    """
    key = (
        str(entity).lower().strip(),
        str(severity).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
