from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("file-server-01", "full"): {
        "system_name": "file-server-01",
        "isolation_level": "full",
        "status": "isolated",
        "network_disconnected": True,
        "services_stopped": True,
        "timestamp": "2024-07-29T08:05:00Z",
        "confirmation": "file-server-01 fully isolated — all network connections severed, services halted",
    },
    ("backup-server-02", "full"): {
        "system_name": "backup-server-02",
        "isolation_level": "full",
        "status": "isolated",
        "network_disconnected": True,
        "services_stopped": True,
        "timestamp": "2024-07-29T08:06:00Z",
        "confirmation": "backup-server-02 fully isolated — all network connections severed, services halted",
    },
    ("customer-db-primary", "full"): {
        "system_name": "customer-db-primary",
        "isolation_level": "full",
        "status": "isolated",
        "network_disconnected": True,
        "services_stopped": True,
        "timestamp": "2024-07-29T06:05:00Z",
        "confirmation": "customer-db-primary fully isolated — all network connections severed, database halted",
    },
    ("workstation-ws-450", "partial"): {
        "system_name": "workstation-WS-450",
        "isolation_level": "partial",
        "status": "isolated",
        "network_disconnected": False,
        "services_stopped": False,
        "timestamp": "2024-07-29T11:05:00Z",
        "confirmation": "workstation-WS-450 partially isolated — external network blocked, internal monitoring active",
    },
    ("workstation-ws-450", "full"): {
        "system_name": "workstation-WS-450",
        "isolation_level": "full",
        "status": "isolated",
        "network_disconnected": True,
        "services_stopped": True,
        "timestamp": "2024-07-29T11:05:00Z",
        "confirmation": "workstation-WS-450 fully isolated — all network connections severed",
    },
    ("email-gateway", "partial"): {
        "system_name": "email-gateway",
        "isolation_level": "partial",
        "status": "isolated",
        "network_disconnected": False,
        "services_stopped": False,
        "timestamp": "2024-07-29T09:35:00Z",
        "confirmation": "email-gateway partially isolated — suspicious domains blocked, legitimate traffic flowing",
    },
}


@tool()
def isolate_system(system_name: str, isolation_level: str):
    """
    Isolates an affected system to contain a security incident.

    Args:
        system_name: The name of the system to isolate (e.g. "file-server-01").
        isolation_level: The level of isolation — one of "full" (all connections severed), "partial" (external blocked, internal monitored), or "monitoring_only".

    Returns:
        Isolation confirmation including status, network state, and timestamp, or None if isolation failed.
    """
    key = (
        str(system_name).lower().strip(),
        str(isolation_level).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
