from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("payments", "critical"): {
        "ticket_id": "INC-1001",
        "service": "payments",
        "severity": "critical",
        "assigned_to": "Pat Rivera",
        "sla_hours": 1,
        "status": "open",
    },
    ("payments", "high"): {
        "ticket_id": "INC-1002",
        "service": "payments",
        "severity": "high",
        "assigned_to": "Pat Rivera",
        "sla_hours": 4,
        "status": "open",
    },
    ("auth", "critical"): {
        "ticket_id": "INC-1003",
        "service": "auth",
        "severity": "critical",
        "assigned_to": "Jordan Kim",
        "sla_hours": 1,
        "status": "open",
    },
    ("auth", "high"): {
        "ticket_id": "INC-1004",
        "service": "auth",
        "severity": "high",
        "assigned_to": "Jordan Kim",
        "sla_hours": 4,
        "status": "open",
    },
    ("frontend", "low"): {
        "ticket_id": "INC-1005",
        "service": "frontend",
        "severity": "low",
        "assigned_to": "Taylor Brooks",
        "sla_hours": 48,
        "status": "open",
    },
}


@tool()
def create_incident_ticket(service_name: str, severity: str, title: str, description: str):
    """
    Creates an incident ticket for tracking and resolution.

    Args:
        service_name: The affected service name (e.g. "payments").
        severity: The incident severity ("critical", "high", "medium", "low").
        title: A short title for the incident.
        description: Detailed description of the incident including symptoms and impact.

    Returns:
        Ticket details including ticket_id, assigned_to, and SLA hours, or None if creation failed.
    """
    key = (
        str(service_name).lower().strip(),
        str(severity).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
