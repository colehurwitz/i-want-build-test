from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("c-100", "account access issue", "account", "high"): {
        "case_id": "CS-300",
        "status": "open",
        "assigned_to": "Support Team A",
        "sla_hours": 4,
        "created_at": "2024-03-15T09:00:00Z",
    },
    ("c-200", "billing dispute", "billing", "normal"): {
        "case_id": "CS-301",
        "status": "open",
        "assigned_to": "Billing Team",
        "sla_hours": 8,
        "created_at": "2024-03-15T09:30:00Z",
    },
    ("c-300", "technical issue - app crashes", "technical", "normal"): {
        "case_id": "CS-302",
        "status": "open",
        "assigned_to": "Support Team B",
        "sla_hours": 8,
        "created_at": "2024-03-15T10:00:00Z",
    },
    ("c-300", "billing question", "billing", "low"): {
        "case_id": "CS-303",
        "status": "open",
        "assigned_to": "Billing Team",
        "sla_hours": 24,
        "created_at": "2024-03-15T10:30:00Z",
    },
}


@tool()
def create_support_case(customer_id: str, subject: str, category: str, priority: str, description: str):
    """
    Creates a new support case for a customer.

    Args:
        customer_id: The unique customer identifier (e.g. "C-100").
        subject: A short summary of the issue.
        category: The case category ("billing", "technical", "account", "product", "general").
        priority: The case priority ("urgent", "high", "normal", "low").
        description: A detailed description of the issue.

    Returns:
        Created case details including case_id, assigned team, and SLA hours, or None if creation failed.
    """
    key = (
        str(customer_id).lower().strip(),
        str(subject).lower().strip(),
        str(category).lower().strip(),
        str(priority).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
