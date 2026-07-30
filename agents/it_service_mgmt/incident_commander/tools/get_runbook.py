from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "payments": {
        "service": "payments",
        "steps": [
            "1. Check payment gateway connectivity",
            "2. Verify database connection pool",
            "3. Check recent deployments for correlation",
            "4. If deployment correlation found, rollback to previous version",
            "5. Notify payments-oncall team",
            "6. Monitor error rate for 15 minutes post-action",
        ],
        "escalation_contacts": ["payments-lead@company.com", "vp-eng@company.com"],
        "rollback_procedure": "Use rollback_deployment with the most recent deploy_id. Target version should be the previous stable release.",
    },
    "auth": {
        "service": "auth",
        "steps": [
            "1. Check auth service latency and error rates",
            "2. Verify session store (Redis) connectivity",
            "3. Check for recent security patches or config changes",
            "4. If latency spike, scale up auth service replicas",
            "5. Notify security-oncall team",
        ],
        "escalation_contacts": ["security-lead@company.com", "cto@company.com"],
        "rollback_procedure": "Auth rollbacks require security team approval. Contact security-lead first.",
    },
    "frontend": {
        "service": "frontend",
        "steps": [
            "1. Check CDN status and cache hit rates",
            "2. Verify origin server health",
            "3. If CDN issue, purge and repopulate cache",
            "4. Monitor for 10 minutes",
        ],
        "escalation_contacts": ["frontend-lead@company.com"],
        "rollback_procedure": "Standard rollback via deploy pipeline.",
    },
}


@tool()
def get_runbook(service_name: str):
    """
    Retrieves the incident response runbook for a service.

    Args:
        service_name: The name of the service (e.g. "payments").

    Returns:
        The runbook with steps, escalation contacts, and rollback procedure, or None if not found.
    """
    normalized = str(service_name).lower().strip()
    return STUB_RESPONSES.get(normalized)
