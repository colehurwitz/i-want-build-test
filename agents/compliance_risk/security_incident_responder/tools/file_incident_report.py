from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("inc-100", "critical", "ransomware"): {
        "report_id": "RPT-8001",
        "incident_id": "INC-100",
        "severity": "critical",
        "type": "ransomware",
        "status": "filed",
        "regulatory_notification_required": False,
        "report_summary": "Ransomware (LockCrypt) detected on file-server-01 with lateral movement to backup-server-02. Both systems isolated. Evidence collected. Threat actor identified as RansomGroup-7.",
        "filed_at": "2024-07-29T09:00:00Z",
        "next_steps": ["Complete forensic analysis", "Restore from clean backups", "Patch exploitation vector"],
    },
    ("inc-200", "high", "phishing"): {
        "report_id": "RPT-8002",
        "incident_id": "INC-200",
        "severity": "high",
        "type": "phishing",
        "status": "filed",
        "regulatory_notification_required": False,
        "report_summary": "Targeted phishing campaign via PhishKit-Pro. 5 employees clicked link, 3 submitted credentials. Credentials reset, domain blocked.",
        "filed_at": "2024-07-29T10:30:00Z",
        "next_steps": ["Monitor for credential reuse", "Conduct phishing awareness training", "Review email filtering rules"],
    },
    ("inc-300", "critical", "data_breach"): {
        "report_id": "RPT-8003",
        "incident_id": "INC-300",
        "severity": "critical",
        "type": "data_breach",
        "status": "filed",
        "regulatory_notification_required": True,
        "notification_deadline": "2024-08-01T06:00:00Z",
        "report_summary": "Data breach via compromised service account. 50,000 PII records exfiltrated to 45.33.32.156. Database isolated, evidence collected.",
        "filed_at": "2024-07-29T07:00:00Z",
        "next_steps": ["Submit GDPR notification within 72 hours", "Engage external forensics firm", "Notify affected customers"],
    },
    ("inc-400", "low", "policy_violation"): {
        "report_id": "RPT-8004",
        "incident_id": "INC-400",
        "severity": "low",
        "type": "policy_violation",
        "status": "filed",
        "regulatory_notification_required": False,
        "report_summary": "VPN credential sharing detected. No malicious activity, policy violation documented for HR review.",
        "filed_at": "2024-07-29T14:30:00Z",
        "next_steps": ["HR to follow up with employee", "Review VPN access policies"],
    },
    ("inc-500", "high", "malware"): {
        "report_id": "RPT-8005",
        "incident_id": "INC-500",
        "severity": "high",
        "type": "malware",
        "status": "filed",
        "regulatory_notification_required": False,
        "report_summary": "Trojan (LockCrypt family) on WS-450 with active C2 to 91.234.100.25. System isolated, 45 MB data exfiltrated. Linked to RansomGroup-7.",
        "filed_at": "2024-07-29T12:00:00Z",
        "next_steps": ["Wipe and reimage workstation", "Scan all systems for related IOCs", "Block C2 infrastructure at firewall"],
    },
    ("inc-600", "medium", "unauthorized_access"): {
        "report_id": "RPT-8006",
        "incident_id": "INC-600",
        "severity": "medium",
        "type": "unauthorized_access",
        "status": "filed",
        "regulatory_notification_required": False,
        "report_summary": "Brute force attempt on admin portal from 103.45.67.89. 500+ failed attempts, no successful breach. IP blocked.",
        "filed_at": "2024-07-29T12:30:00Z",
        "next_steps": ["Review admin portal authentication hardening", "Implement rate limiting"],
    },
}


@tool()
def file_incident_report(incident_id: str, severity: str, type: str, root_cause: str, remediation: str, evidence_ids: list):
    """
    Files a comprehensive incident report with evidence and remediation details.

    Args:
        incident_id: The incident identifier (e.g. "INC-100").
        severity: The incident severity — one of "critical", "high", "medium", or "low".
        type: The incident type (e.g. "ransomware", "phishing", "data_breach", "malware", "unauthorized_access", "policy_violation").
        root_cause: Description of the root cause of the incident.
        remediation: Remediation steps taken or planned.
        evidence_ids: List of evidence IDs collected during investigation (e.g. ["EVD-7001", "EVD-7002"]).

    Returns:
        Filed report including report_id, status, regulatory notification requirements, and next steps, or None if filing failed.
    """
    key = (
        str(incident_id).lower().strip(),
        str(severity).lower().strip(),
        str(type).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
