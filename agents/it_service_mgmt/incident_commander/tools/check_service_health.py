from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "payments": {
        "service": "payments",
        "status": "down",
        "latency_ms": None,
        "error_rate": 100.0,
        "uptime_pct": 99.2,
        "last_healthy": "2024-07-29T10:10:00Z",
    },
    "auth": {
        "service": "auth",
        "status": "degraded",
        "latency_ms": 5200,
        "error_rate": 8.5,
        "uptime_pct": 99.5,
        "last_healthy": "2024-07-29T11:25:00Z",
    },
    "frontend": {
        "service": "frontend",
        "status": "healthy",
        "latency_ms": 120,
        "error_rate": 0.1,
        "uptime_pct": 99.99,
        "last_healthy": "2024-07-29T12:00:00Z",
    },
}


@tool()
def check_service_health(service_name: str):
    """
    Checks the current health status of a service.

    Args:
        service_name: The name of the service to check (e.g. "payments").

    Returns:
        Service health details including status, latency, error rate, and uptime, or None if service not found.
    """
    normalized = str(service_name).lower().strip()
    return STUB_RESPONSES.get(normalized)
