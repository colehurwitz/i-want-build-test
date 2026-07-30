from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("185.141.63.120", "ip"): {
        "indicator": "185.141.63.120",
        "indicator_type": "ip",
        "threat_level": "critical",
        "known_threat": True,
        "threat_actor": "RansomGroup-7",
        "malware_family": "LockCrypt",
        "first_seen": "2024-01-15",
        "last_seen": "2024-07-28",
        "related_indicators": ["suspicious_executable.exe", "91.234.100.25", "encrypt_payload.bin"],
        "recommended_action": "Block immediately, full system isolation required",
    },
    ("hxxps://login-portal.evil.com/auth", "url"): {
        "indicator": "hxxps://login-portal.evil.com/auth",
        "indicator_type": "url",
        "threat_level": "high",
        "known_threat": True,
        "threat_actor": "PhishKit-Pro",
        "malware_family": None,
        "first_seen": "2024-07-25",
        "last_seen": "2024-07-29",
        "related_indicators": ["phish@spoofed-domain.com", "login-portal.evil.com"],
        "recommended_action": "Block domain, reset credentials for affected users",
    },
    ("45.33.32.156", "ip"): {
        "indicator": "45.33.32.156",
        "indicator_type": "ip",
        "threat_level": "high",
        "known_threat": True,
        "threat_actor": "DataHarvest",
        "malware_family": None,
        "first_seen": "2024-03-10",
        "last_seen": "2024-07-29",
        "related_indicators": ["data-exfil-tool.py", "45.33.32.157"],
        "recommended_action": "Block IP range, investigate all connections from this source",
    },
    ("91.234.100.25", "ip"): {
        "indicator": "91.234.100.25",
        "indicator_type": "ip",
        "threat_level": "critical",
        "known_threat": True,
        "threat_actor": "RansomGroup-7",
        "malware_family": "LockCrypt",
        "first_seen": "2024-02-20",
        "last_seen": "2024-07-29",
        "related_indicators": ["trojan_dropper.dll", "185.141.63.120", "c2-beacon.exe"],
        "recommended_action": "Block immediately, associated with active ransomware campaign",
    },
    ("103.45.67.89", "ip"): {
        "indicator": "103.45.67.89",
        "indicator_type": "ip",
        "threat_level": "medium",
        "known_threat": True,
        "threat_actor": "Unknown",
        "malware_family": None,
        "first_seen": "2024-06-01",
        "last_seen": "2024-07-29",
        "related_indicators": [],
        "recommended_action": "Block IP, known scanner/brute force source",
    },
}


@tool()
def get_threat_intel(indicator: str, indicator_type: str):
    """
    Retrieves threat intelligence for a given indicator of compromise.

    Args:
        indicator: The indicator value (e.g. an IP address, URL, or file hash).
        indicator_type: The type of indicator — one of "ip", "url", "domain", or "hash".

    Returns:
        Threat intelligence data including threat level, known threat actor, malware family, related indicators, and recommended action, or None if not found.
    """
    key = (str(indicator).lower().strip(), str(indicator_type).lower().strip())
    return STUB_RESPONSES.get(key)
