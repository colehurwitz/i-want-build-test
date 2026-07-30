from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("payments", "24"): [
        {
            "deploy_id": "DEP-501",
            "version": "v3.2.1",
            "deployer": "deploy-bot",
            "timestamp": "2024-07-29T09:45:00Z",
            "status": "completed",
            "change_summary": "Updated payment gateway integration",
        },
        {
            "deploy_id": "DEP-500",
            "version": "v3.2.0",
            "deployer": "alice@company.com",
            "timestamp": "2024-07-28T16:00:00Z",
            "status": "completed",
            "change_summary": "Added new currency support",
        },
    ],
    ("auth", "24"): [],
    ("frontend", "24"): [
        {
            "deploy_id": "DEP-490",
            "version": "v2.8.0",
            "deployer": "bob@company.com",
            "timestamp": "2024-07-28T14:30:00Z",
            "status": "completed",
            "change_summary": "Updated CDN configuration",
        },
    ],
    ("payments", "48"): [
        {
            "deploy_id": "DEP-501",
            "version": "v3.2.1",
            "deployer": "deploy-bot",
            "timestamp": "2024-07-29T09:45:00Z",
            "status": "completed",
            "change_summary": "Updated payment gateway integration",
        },
        {
            "deploy_id": "DEP-500",
            "version": "v3.2.0",
            "deployer": "alice@company.com",
            "timestamp": "2024-07-28T16:00:00Z",
            "status": "completed",
            "change_summary": "Added new currency support",
        },
    ],
    ("auth", "48"): [
        {
            "deploy_id": "DEP-480",
            "version": "v1.9.5",
            "deployer": "carol@company.com",
            "timestamp": "2024-07-27T10:00:00Z",
            "status": "completed",
            "change_summary": "Security patch for token validation",
        },
    ],
}


@tool()
def get_recent_deployments(service_name: str, hours: int):
    """
    Retrieves recent deployments for a service within a specified time window.

    Args:
        service_name: The name of the service (e.g. "payments").
        hours: Number of hours to look back for deployments.

    Returns:
        A list of deployment records with deploy_id, version, deployer, and timestamp, or None if not found.
    """
    key = (
        str(service_name).lower().strip(),
        str(hours).strip(),
    )
    return STUB_RESPONSES.get(key)
