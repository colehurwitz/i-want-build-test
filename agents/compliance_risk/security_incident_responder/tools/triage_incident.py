from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "inc-100": {
        "incident_id": "INC-100",
        "severity": "P1",
        "type": "ransomware",
        "status": "active",
        "affected_systems": ["file-server-01", "backup-server-02"],
        "detected_at": "2024-07-29T08:00:00Z",
        "description": "Ransomware detected on file-server-01, encryption in progress. Lateral movement to backup-server-02 suspected.",
        "indicators": ["suspicious_executable.exe", "185.141.63.120"],
        "recommended_actions": ["Immediately isolate affected systems", "Collect evidence before remediation", "Notify CISO and legal"],
    },
    "inc-200": {
        "incident_id": "INC-200",
        "severity": "P2",
        "type": "phishing",
        "status": "active",
        "affected_systems": ["email-gateway"],
        "detected_at": "2024-07-29T09:30:00Z",
        "description": "Targeted phishing campaign detected. 5 employees clicked malicious link at hxxps://login-portal.evil.com/auth.",
        "indicators": ["hxxps://login-portal.evil.com/auth", "phish@spoofed-domain.com"],
        "recommended_actions": ["Check threat intel for phishing URL", "Collect evidence from email gateway", "Notify affected department heads"],
    },
    "inc-300": {
        "incident_id": "INC-300",
        "severity": "P1",
        "type": "data_breach",
        "status": "active",
        "affected_systems": ["customer-db-primary"],
        "detected_at": "2024-07-29T06:00:00Z",
        "description": "Unauthorized data exfiltration detected from customer database. Approximately 50,000 PII records accessed.",
        "indicators": ["45.33.32.156", "unusual SQL queries"],
        "recommended_actions": ["Isolate database immediately", "Collect network_logs and access_logs", "Notify CISO, legal, and executive team", "Regulatory notification required within 72 hours"],
        "regulatory_notification_required": True,
    },
    "inc-400": {
        "incident_id": "INC-400",
        "severity": "P4",
        "type": "policy_violation",
        "status": "active",
        "affected_systems": ["vpn-gateway"],
        "detected_at": "2024-07-29T14:00:00Z",
        "description": "Employee sharing VPN credentials with contractor. No malicious activity detected.",
        "indicators": ["concurrent VPN sessions from different geolocations"],
        "recommended_actions": ["Check threat intel for IPs", "File report for policy team review"],
    },
    "inc-500": {
        "incident_id": "INC-500",
        "severity": "P2",
        "type": "malware",
        "status": "active",
        "affected_systems": ["workstation-WS-450"],
        "detected_at": "2024-07-29T11:00:00Z",
        "description": "Trojan detected on workstation WS-450. Command and control communication observed to 91.234.100.25.",
        "indicators": ["trojan_dropper.dll", "91.234.100.25"],
        "recommended_actions": ["Isolate workstation", "Collect memory dump and disk image", "Check threat intel for C2 IP"],
    },
    "inc-600": {
        "incident_id": "INC-600",
        "severity": "P3",
        "type": "unauthorized_access",
        "status": "active",
        "affected_systems": ["admin-portal"],
        "detected_at": "2024-07-29T11:15:00Z",
        "description": "Brute force login attempts detected on admin portal. 500+ failed attempts from single IP.",
        "indicators": ["103.45.67.89"],
        "recommended_actions": ["Check threat intel for attacking IP", "Collect access logs", "Notify security team"],
    },
}


@tool()
def triage_incident(incident_id: str):
    """
    Triages a security incident to assess its severity, type, and recommended response actions.

    Args:
        incident_id: The incident identifier (e.g. "INC-100").

    Returns:
        Incident triage data including severity (P1-P4), type, affected systems, indicators of compromise, and recommended actions, or None if not found.
    """
    normalized = str(incident_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
