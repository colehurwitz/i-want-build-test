from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "c-100": {
        "customer_id": "C-100",
        "name": "Acme Corp",
        "plan": "enterprise",
        "account_age_months": 24,
        "total_cases": 8,
        "open_cases": 1,
        "recent_cases": [
            {"case_id": "CS-150", "subject": "Login timeout issues", "status": "resolved", "created_date": "2024-02-10"},
            {"case_id": "CS-120", "subject": "SSO configuration", "status": "resolved", "created_date": "2024-01-15"},
        ],
        "satisfaction_score": 4.2,
    },
    "c-200": {
        "customer_id": "C-200",
        "name": "SmallBiz LLC",
        "plan": "pro",
        "account_age_months": 6,
        "total_cases": 3,
        "open_cases": 0,
        "recent_cases": [
            {"case_id": "CS-180", "subject": "Billing charge dispute", "status": "resolved", "created_date": "2024-02-20"},
        ],
        "satisfaction_score": 3.5,
    },
    "c-300": {
        "customer_id": "C-300",
        "name": "TechStart Inc",
        "plan": "free",
        "account_age_months": 2,
        "total_cases": 1,
        "open_cases": 0,
        "recent_cases": [
            {"case_id": "CS-190", "subject": "Feature request", "status": "closed", "created_date": "2024-03-01"},
        ],
        "satisfaction_score": 3.0,
    },
    "c-400": {
        "customer_id": "C-400",
        "name": "MegaCorp Global",
        "plan": "enterprise",
        "account_age_months": 36,
        "total_cases": 15,
        "open_cases": 2,
        "recent_cases": [
            {"case_id": "CS-195", "subject": "API rate limiting", "status": "open", "created_date": "2024-03-10"},
            {"case_id": "CS-192", "subject": "Data export timeout", "status": "open", "created_date": "2024-03-05"},
        ],
        "satisfaction_score": 3.8,
    },
    "c-500": {
        "customer_id": "C-500",
        "name": "Startup Fresh",
        "plan": "pro",
        "account_age_months": 1,
        "total_cases": 0,
        "open_cases": 0,
        "recent_cases": [],
        "satisfaction_score": None,
    },
}


@tool()
def get_customer_history(customer_id: str):
    """
    Retrieves a customer's support history including past cases and satisfaction scores.

    Args:
        customer_id: The unique customer identifier (e.g. "C-100").

    Returns:
        Customer history including plan, account age, case history, and satisfaction score, or None if not found.
    """
    normalized = str(customer_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
