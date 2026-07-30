from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("inc-100", "critical"): {
        "incident_id": "INC-100",
        "severity": "critical",
        "notifications_sent": [
            {"group": "ciso", "method": "page", "status": "delivered", "timestamp": "2024-07-29T08:07:00Z"},
            {"group": "legal", "method": "email", "status": "delivered", "timestamp": "2024-07-29T08:07:01Z"},
            {"group": "executive_team", "method": "email", "status": "delivered", "timestamp": "2024-07-29T08:07:02Z"},
        ],
        "confirmation": "All critical stakeholders notified for INC-100",
    },
    ("inc-200", "high"): {
        "incident_id": "INC-200",
        "severity": "high",
        "notifications_sent": [
            {"group": "security_team", "method": "slack", "status": "delivered", "timestamp": "2024-07-29T09:45:00Z"},
            {"group": "affected_departments", "method": "email", "status": "delivered", "timestamp": "2024-07-29T09:45:01Z"},
        ],
        "confirmation": "High-severity stakeholders notified for INC-200",
    },
    ("inc-300", "critical"): {
        "incident_id": "INC-300",
        "severity": "critical",
        "notifications_sent": [
            {"group": "ciso", "method": "page", "status": "delivered", "timestamp": "2024-07-29T06:15:00Z"},
            {"group": "legal", "method": "page", "status": "delivered", "timestamp": "2024-07-29T06:15:01Z"},
            {"group": "executive_team", "method": "email", "status": "delivered", "timestamp": "2024-07-29T06:15:02Z"},
        ],
        "confirmation": "All critical stakeholders notified for INC-300 — regulatory notification deadline: 72 hours",
    },
    ("inc-400", "low"): {
        "incident_id": "INC-400",
        "severity": "low",
        "notifications_sent": [
            {"group": "security_team", "method": "email", "status": "delivered", "timestamp": "2024-07-29T14:10:00Z"},
        ],
        "confirmation": "Security team notified via normal channels for INC-400",
    },
    ("inc-500", "high"): {
        "incident_id": "INC-500",
        "severity": "high",
        "notifications_sent": [
            {"group": "security_team", "method": "slack", "status": "delivered", "timestamp": "2024-07-29T11:15:00Z"},
            {"group": "it_department", "method": "email", "status": "delivered", "timestamp": "2024-07-29T11:15:01Z"},
        ],
        "confirmation": "High-severity stakeholders notified for INC-500",
    },
}


@tool()
def notify_stakeholders(incident_id: str, severity: str, stakeholder_groups: list, message: str):
    """
    Notifies relevant stakeholders about a security incident based on severity.

    Args:
        incident_id: The incident identifier (e.g. "INC-100").
        severity: The incident severity — one of "critical", "high", "medium", or "low".
        stakeholder_groups: List of stakeholder groups to notify (e.g. ["ciso", "legal", "executive_team"]).
        message: The notification message describing the incident and current status.

    Returns:
        Notification confirmation including list of notifications sent with delivery status, or None if notification failed.
    """
    key = (
        str(incident_id).lower().strip(),
        str(severity).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
