from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("auth_system", "unauthorized_access", "critical"): {
        "finding_id": "FND-2001",
        "system": "auth_system",
        "finding_type": "unauthorized_access",
        "severity": "critical",
        "status": "flagged",
        "assigned_to": "security-team",
        "escalation": "immediate — CISO notified",
        "created_at": "2024-07-29T10:00:00Z",
    },
    ("auth_system", "privilege_escalation", "critical"): {
        "finding_id": "FND-2002",
        "system": "auth_system",
        "finding_type": "privilege_escalation",
        "severity": "critical",
        "status": "flagged",
        "assigned_to": "security-team",
        "escalation": "immediate — CISO notified",
        "created_at": "2024-07-29T10:01:00Z",
    },
    ("auth_system", "unusual_hours", "medium"): {
        "finding_id": "FND-2003",
        "system": "auth_system",
        "finding_type": "unusual_hours",
        "severity": "medium",
        "status": "flagged",
        "assigned_to": "audit-team",
        "escalation": "standard review queue",
        "created_at": "2024-07-29T10:02:00Z",
    },
    ("payment_system", "data_exfiltration", "medium"): {
        "finding_id": "FND-2004",
        "system": "payment_system",
        "finding_type": "data_exfiltration",
        "severity": "medium",
        "status": "flagged",
        "assigned_to": "finance-audit-team",
        "escalation": "standard review queue",
        "created_at": "2024-07-29T10:03:00Z",
    },
}


@tool()
def flag_finding(system: str, finding_type: str, severity: str, description: str, evidence: str):
    """
    Flags an audit finding with severity and supporting evidence.

    Args:
        system: The system where the finding was detected (e.g. "auth_system").
        finding_type: The type of finding — one of "unauthorized_access", "data_exfiltration", "privilege_escalation", or "unusual_hours".
        severity: The severity level — one of "critical", "high", "medium", or "low".
        description: A description of the finding.
        evidence: Supporting evidence including log entries, timestamps, and IP addresses.

    Returns:
        Finding record including finding_id, status, assigned team, and escalation action, or None if flagging failed.
    """
    key = (
        str(system).lower().strip(),
        str(finding_type).lower().strip(),
        str(severity).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
