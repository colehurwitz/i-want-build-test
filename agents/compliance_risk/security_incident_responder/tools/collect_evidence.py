from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("inc-100", "file-server-01", "memory_dump"): {
        "evidence_id": "EVD-7001",
        "incident_id": "INC-100",
        "system_name": "file-server-01",
        "evidence_type": "memory_dump",
        "size_mb": 4096,
        "hash_sha256": "a1b2c3d4e5f6...",
        "collected_by": "automated_ir_system",
        "collected_at": "2024-07-29T08:10:00Z",
        "chain_of_custody": "Collected by IR automation, stored in evidence vault EVD-VAULT-01",
        "findings": "Ransomware process 'suspicious_executable.exe' found in memory, encryption key material recovered",
    },
    ("inc-100", "file-server-01", "disk_image"): {
        "evidence_id": "EVD-7002",
        "incident_id": "INC-100",
        "system_name": "file-server-01",
        "evidence_type": "disk_image",
        "size_mb": 512000,
        "hash_sha256": "f6e5d4c3b2a1...",
        "collected_by": "automated_ir_system",
        "collected_at": "2024-07-29T08:30:00Z",
        "chain_of_custody": "Collected by IR automation, stored in evidence vault EVD-VAULT-01",
        "findings": "42% of files encrypted, ransomware dropper found in /tmp/",
    },
    ("inc-200", "email-gateway", "network_logs"): {
        "evidence_id": "EVD-7003",
        "incident_id": "INC-200",
        "system_name": "email-gateway",
        "evidence_type": "network_logs",
        "size_mb": 250,
        "hash_sha256": "b2c3d4e5f6a1...",
        "collected_by": "automated_ir_system",
        "collected_at": "2024-07-29T09:40:00Z",
        "chain_of_custody": "Collected by IR automation, stored in evidence vault EVD-VAULT-01",
        "findings": "5 outbound connections to login-portal.evil.com, credentials submitted by 3 unique users",
    },
    ("inc-300", "customer-db-primary", "network_logs"): {
        "evidence_id": "EVD-7004",
        "incident_id": "INC-300",
        "system_name": "customer-db-primary",
        "evidence_type": "network_logs",
        "size_mb": 800,
        "hash_sha256": "c3d4e5f6a1b2...",
        "collected_by": "automated_ir_system",
        "collected_at": "2024-07-29T06:10:00Z",
        "chain_of_custody": "Collected by IR automation, stored in evidence vault EVD-VAULT-01",
        "findings": "Large data transfer (2.3 GB) to external IP 45.33.32.156 over 4-hour period",
    },
    ("inc-300", "customer-db-primary", "access_logs"): {
        "evidence_id": "EVD-7005",
        "incident_id": "INC-300",
        "system_name": "customer-db-primary",
        "evidence_type": "access_logs",
        "size_mb": 150,
        "hash_sha256": "d4e5f6a1b2c3...",
        "collected_by": "automated_ir_system",
        "collected_at": "2024-07-29T06:12:00Z",
        "chain_of_custody": "Collected by IR automation, stored in evidence vault EVD-VAULT-01",
        "findings": "Unauthorized SQL queries from compromised service account SA-DB-READER, 50,000 customer records accessed",
    },
    ("inc-500", "workstation-ws-450", "memory_dump"): {
        "evidence_id": "EVD-7006",
        "incident_id": "INC-500",
        "system_name": "workstation-WS-450",
        "evidence_type": "memory_dump",
        "size_mb": 2048,
        "hash_sha256": "e5f6a1b2c3d4...",
        "collected_by": "automated_ir_system",
        "collected_at": "2024-07-29T11:10:00Z",
        "chain_of_custody": "Collected by IR automation, stored in evidence vault EVD-VAULT-01",
        "findings": "Trojan dropper active in memory, C2 beacon sending data every 60 seconds to 91.234.100.25",
    },
    ("inc-500", "workstation-ws-450", "network_logs"): {
        "evidence_id": "EVD-7007",
        "incident_id": "INC-500",
        "system_name": "workstation-WS-450",
        "evidence_type": "network_logs",
        "size_mb": 120,
        "hash_sha256": "f6a1b2c3d4e5...",
        "collected_by": "automated_ir_system",
        "collected_at": "2024-07-29T11:12:00Z",
        "chain_of_custody": "Collected by IR automation, stored in evidence vault EVD-VAULT-01",
        "findings": "Persistent C2 communication to 91.234.100.25 on port 443, 45 MB exfiltrated over 6 hours",
    },
}


@tool()
def collect_evidence(incident_id: str, system_name: str, evidence_type: str):
    """
    Collects forensic evidence from a system involved in a security incident.

    Args:
        incident_id: The incident identifier (e.g. "INC-100").
        system_name: The system to collect evidence from (e.g. "file-server-01").
        evidence_type: The type of evidence to collect — one of "network_logs", "memory_dump", "disk_image", or "access_logs".

    Returns:
        Evidence record including evidence_id, hash, chain of custody, and preliminary findings, or None if collection failed.
    """
    key = (
        str(incident_id).lower().strip(),
        str(system_name).lower().strip(),
        str(evidence_type).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
