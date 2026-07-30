from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("auth_system", "unauthorized_access"): {
        "system": "auth_system",
        "anomaly_type": "unauthorized_access",
        "anomalies_found": 2,
        "details": [
            {
                "timestamp": "2024-07-23T03:14:00Z",
                "user": "U-500",
                "description": "Login from known TOR exit node (185.220.101.42) followed by immediate privilege escalation",
                "risk_score": 9.2,
                "ip": "185.220.101.42",
            },
            {
                "timestamp": "2024-07-27T01:00:00Z",
                "user": "U-500",
                "description": "Failed login attempts (15) from multiple IPs within 5 minutes",
                "risk_score": 7.5,
                "ip": "various",
            },
        ],
    },
    ("auth_system", "unusual_hours"): {
        "system": "auth_system",
        "anomaly_type": "unusual_hours",
        "anomalies_found": 1,
        "details": [
            {
                "timestamp": "2024-07-25T02:30:00Z",
                "user": "U-302",
                "description": "Bulk data export at 2:30 AM — user typically active 9 AM to 6 PM",
                "risk_score": 6.8,
                "ip": "10.0.1.55",
            },
        ],
    },
    ("auth_system", "privilege_escalation"): {
        "system": "auth_system",
        "anomaly_type": "privilege_escalation",
        "anomalies_found": 1,
        "details": [
            {
                "timestamp": "2024-07-23T03:15:00Z",
                "user": "U-500",
                "description": "Self-elevated to admin role without approval workflow — bypassed standard access request",
                "risk_score": 9.5,
                "ip": "185.220.101.42",
            },
        ],
    },
    ("auth_system", "data_exfiltration"): {
        "system": "auth_system",
        "anomaly_type": "data_exfiltration",
        "anomalies_found": 0,
        "details": [],
    },
    ("payment_system", "unauthorized_access"): {
        "system": "payment_system",
        "anomaly_type": "unauthorized_access",
        "anomalies_found": 0,
        "details": [],
    },
    ("payment_system", "data_exfiltration"): {
        "system": "payment_system",
        "anomaly_type": "data_exfiltration",
        "anomalies_found": 1,
        "details": [
            {
                "timestamp": "2024-07-25T14:30:00Z",
                "user": "U-401",
                "description": "Repetitive daily refund pattern — 3 refunds on consecutive days totaling $525",
                "risk_score": 5.5,
                "ip": "10.0.2.20",
            },
        ],
    },
}


@tool()
def search_anomalies(system: str, anomaly_type: str):
    """
    Searches for anomalies of a specific type in a system's audit trail.

    Args:
        system: The system name to search (e.g. "auth_system", "payment_system").
        anomaly_type: The type of anomaly to search for — one of "unauthorized_access", "data_exfiltration", "privilege_escalation", or "unusual_hours".

    Returns:
        Anomaly search results including count and details (timestamp, user, description, risk_score, IP) for each anomaly found, or None if not found.
    """
    key = (
        str(system).lower().strip(),
        str(anomaly_type).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
