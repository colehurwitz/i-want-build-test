from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "dep-501": {
        "status": "success",
        "deploy_id": "DEP-501",
        "rolled_back_to_version": "v3.2.0",
        "rollback_time": "2024-07-29T10:20:00Z",
        "message": "Successfully rolled back payments service from v3.2.1 to v3.2.0",
    },
    "dep-500": {
        "status": "success",
        "deploy_id": "DEP-500",
        "rolled_back_to_version": "v3.1.9",
        "rollback_time": "2024-07-29T10:25:00Z",
        "message": "Successfully rolled back payments service from v3.2.0 to v3.1.9",
    },
    "dep-490": {
        "status": "success",
        "deploy_id": "DEP-490",
        "rolled_back_to_version": "v2.7.5",
        "rollback_time": "2024-07-29T12:05:00Z",
        "message": "Successfully rolled back frontend service from v2.8.0 to v2.7.5",
    },
}


@tool()
def rollback_deployment(deploy_id: str):
    """
    Rolls back a deployment to the previous version.

    Args:
        deploy_id: The deployment ID to roll back (e.g. "DEP-501").

    Returns:
        Rollback result including status, rolled-back-to version, and confirmation message, or None if deployment not found.
    """
    normalized = str(deploy_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
