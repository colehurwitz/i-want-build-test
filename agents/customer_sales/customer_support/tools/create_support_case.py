from ibm_watsonx_orchestrate.agent_builder.tools import tool

_CS300 = {
    "case_id": "CS-300",
    "status": "open",
    "assigned_to": "Support Team A",
    "sla_hours": 4,
    "created_at": "2024-03-15T09:00:00Z",
}
_CS301 = {
    "case_id": "CS-301",
    "status": "open",
    "assigned_to": "Billing Team",
    "sla_hours": 8,
    "created_at": "2024-03-15T09:30:00Z",
}
_CS302 = {
    "case_id": "CS-302",
    "status": "open",
    "assigned_to": "Support Team B",
    "sla_hours": 8,
    "created_at": "2024-03-15T10:00:00Z",
}
_CS303 = {
    "case_id": "CS-303",
    "status": "open",
    "assigned_to": "Billing Team",
    "sla_hours": 24,
    "created_at": "2024-03-15T10:30:00Z",
}

STUB_RESPONSES = {
    ("c-100", "account access issue", "account", "high"): _CS300,
    ("c-100", "account access issue for c-100", "account", "high"): _CS300,
    ("c-100", "account access issue - c-100", "account", "high"): _CS300,
    ("c-100", "customer cannot access account", "account", "high"): _CS300,
    ("c-100", "unable to access account", "account", "high"): _CS300,
    ("c-100", "login issue", "account", "high"): _CS300,
    ("c-100", "account login issue", "account", "high"): _CS300,
    ("c-200", "billing dispute", "billing", "normal"): _CS301,
    ("c-200", "billing dispute for recent charges", "billing", "normal"): _CS301,
    ("c-200", "billing dispute - c-200", "billing", "normal"): _CS301,
    ("c-200", "billing dispute for c-200", "billing", "normal"): _CS301,
    ("c-200", "charge dispute", "billing", "normal"): _CS301,
    ("c-200", "invoice dispute", "billing", "normal"): _CS301,
    ("c-200", "billing dispute", "billing", "high"): _CS301,
    ("c-200", "billing dispute for recent charges", "billing", "high"): _CS301,
    ("c-300", "technical issue - app crashes", "technical", "normal"): _CS302,
    ("c-300", "technical issue reported by techstart inc", "technical", "normal"): _CS302,
    ("c-300", "technical issue reported by techstart inc", "technical", "high"): _CS302,
    ("c-300", "application crash", "technical", "normal"): _CS302,
    ("c-300", "application crash", "technical", "high"): _CS302,
    ("c-300", "app crash", "technical", "normal"): _CS302,
    ("c-300", "app crash on dashboard", "technical", "normal"): _CS302,
    ("c-300", "technical issue", "technical", "normal"): _CS302,
    ("c-300", "technical issue", "technical", "high"): _CS302,
    ("c-300", "dashboard crash", "technical", "normal"): _CS302,
    ("c-300", "billing question", "billing", "low"): _CS303,
    ("c-300", "billing question from techstart inc", "billing", "low"): _CS303,
    ("c-300", "billing question from techstart inc", "billing", "normal"): _CS303,
    ("c-300", "billing inquiry", "billing", "low"): _CS303,
    ("c-300", "billing inquiry", "billing", "normal"): _CS303,
    ("c-300", "invoice question", "billing", "low"): _CS303,
    ("c-300", "invoice question", "billing", "normal"): _CS303,
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
