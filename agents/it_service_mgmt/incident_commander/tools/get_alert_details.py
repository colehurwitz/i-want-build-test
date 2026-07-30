from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "a-100": {
        "alert_id": "A-100",
        "service": "payments",
        "severity": "critical",
        "message": "Payment processing service is DOWN — all transactions failing",
        "timestamp": "2024-07-29T10:15:00Z",
        "metric_value": "0% success rate",
    },
    "a-200": {
        "alert_id": "A-200",
        "service": "auth",
        "severity": "high",
        "message": "Authentication service latency spike — p99 > 5000ms",
        "timestamp": "2024-07-29T11:30:00Z",
        "metric_value": "p99 latency: 5200ms",
    },
    "a-300": {
        "alert_id": "A-300",
        "service": "frontend",
        "severity": "low",
        "message": "Frontend CDN cache miss rate elevated",
        "timestamp": "2024-07-29T12:00:00Z",
        "metric_value": "cache miss rate: 15%",
    },
    "a-400": {
        "alert_id": "A-400",
        "service": "payments",
        "severity": "high",
        "message": "Payment service error rate elevated",
        "timestamp": "2024-07-29T13:00:00Z",
        "metric_value": "error rate: 12%",
    },
    "a-401": {
        "alert_id": "A-401",
        "service": "auth",
        "severity": "critical",
        "message": "Auth service completely unresponsive",
        "timestamp": "2024-07-29T13:01:00Z",
        "metric_value": "0 responses",
    },
    "a-500": {
        "alert_id": "A-500",
        "service": "payments",
        "severity": "critical",
        "message": "Payment service error rate critically high",
        "timestamp": "2024-07-29T14:00:00Z",
        "metric_value": "error rate: 45%",
    },
}


@tool()
def get_alert_details(alert_id: str):
    """
    Retrieves details for a specific alert.

    Args:
        alert_id: The alert identifier (e.g. "A-100").

    Returns:
        Alert details including service, severity, message, timestamp, and metric value, or None if not found.
    """
    normalized = str(alert_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
