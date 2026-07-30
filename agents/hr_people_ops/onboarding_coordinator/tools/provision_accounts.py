from ibm_watsonx_orchestrate.agent_builder.tools import tool
from typing import List

STUB_RESPONSES = {
    "e-500": {
        "employee_id": "E-500",
        "provisioned": ["email", "vpn", "slack", "github", "jira", "aws_console"],
        "failed": [],
        "status": "complete",
    },
    "e-501": {
        "employee_id": "E-501",
        "provisioned": ["email", "vpn", "slack", "salesforce"],
        "failed": ["zoom_pro"],
        "status": "partial",
        "failure_reason": "Zoom Pro license limit reached. Contact IT for additional licenses.",
    },
    "e-502": {
        "employee_id": "E-502",
        "provisioned": ["email", "vpn", "slack", "github", "jira", "aws_console"],
        "failed": [],
        "status": "complete",
    },
    "e-503": {
        "employee_id": "E-503",
        "provisioned": ["email", "vpn", "slack", "github", "jira", "aws_console"],
        "failed": [],
        "status": "complete",
    },
    "e-504": {
        "employee_id": "E-504",
        "provisioned": ["email", "vpn", "slack", "github", "jira", "aws_console"],
        "failed": [],
        "status": "complete",
    },
}


@tool()
def provision_accounts(employee_id: str, account_types: list):
    """
    Provisions system accounts for a new employee.

    Args:
        employee_id: The new employee's ID (e.g. "E-500").
        account_types: List of account types to provision (e.g. ["email", "vpn", "slack", "github"]).

    Returns:
        The provisioning results showing which accounts were successfully created and which failed, or None if the employee is not found.
    """
    normalized = str(employee_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
