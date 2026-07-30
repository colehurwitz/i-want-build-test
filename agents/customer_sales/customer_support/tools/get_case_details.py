from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "cs-200": {
        "case_id": "CS-200",
        "customer_id": "C-400",
        "subject": "API integration errors",
        "category": "technical",
        "priority": "high",
        "status": "open",
        "description": "Customer reporting 500 errors on API calls since yesterday",
        "assigned_to": "Support Team A",
        "created_at": "2024-03-13T14:00:00Z",
        "sla_hours": 4,
    },
    "cs-300": {
        "case_id": "CS-300",
        "customer_id": "C-100",
        "subject": "Account access issue",
        "category": "account",
        "priority": "high",
        "status": "open",
        "description": "Customer cannot access their account dashboard",
        "assigned_to": "Support Team A",
        "created_at": "2024-03-15T09:00:00Z",
        "sla_hours": 4,
    },
    "cs-400": {
        "case_id": "CS-400",
        "customer_id": "C-200",
        "subject": "Subscription downgrade request",
        "category": "billing",
        "priority": "normal",
        "status": "open",
        "description": "Customer wants to downgrade from Pro to Free tier",
        "assigned_to": "Billing Team",
        "created_at": "2024-03-14T11:00:00Z",
        "sla_hours": 8,
    },
}


@tool()
def get_case_details(case_id: str):
    """
    Retrieves detailed information about a support case.

    Args:
        case_id: The unique case identifier (e.g. "CS-200").

    Returns:
        Case details including customer, subject, category, priority, status, and SLA info, or None if not found.
    """
    normalized = str(case_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
