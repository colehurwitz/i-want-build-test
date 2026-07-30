from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "a-100": {
        "account_id": "A-100",
        "contract_id": "CTR-1001",
        "start_date": "2023-01-01",
        "end_date": "2025-01-01",
        "auto_renew": True,
        "annual_value": 250000.00,
        "payment_terms": "net_30",
        "products": ["platform_enterprise", "analytics_pro", "automation_suite"],
        "discount_pct": 10.0,
        "renewal_status": "auto_renew_active",
    },
    "a-200": {
        "account_id": "A-200",
        "contract_id": "CTR-1002",
        "start_date": "2022-06-01",
        "end_date": "2024-06-01",
        "auto_renew": False,
        "annual_value": 180000.00,
        "payment_terms": "net_45",
        "products": ["platform_enterprise", "reporting_basic"],
        "discount_pct": 5.0,
        "renewal_status": "pending_renewal",
    },
    "a-300": {
        "account_id": "A-300",
        "contract_id": "CTR-1003",
        "start_date": "2023-07-01",
        "end_date": "2024-07-01",
        "auto_renew": False,
        "annual_value": 75000.00,
        "payment_terms": "net_30",
        "products": ["platform_standard", "analytics_basic"],
        "discount_pct": 0.0,
        "renewal_status": "pending_renewal",
    },
    "a-400": {
        "account_id": "A-400",
        "contract_id": "CTR-1004",
        "start_date": "2023-03-01",
        "end_date": "2026-03-01",
        "auto_renew": True,
        "annual_value": 320000.00,
        "payment_terms": "net_30",
        "products": ["platform_enterprise", "analytics_pro", "automation_suite", "integrations_premium"],
        "discount_pct": 15.0,
        "renewal_status": "auto_renew_active",
    },
    "a-500": {
        "account_id": "A-500",
        "contract_id": "CTR-1005",
        "start_date": "2023-09-01",
        "end_date": "2024-09-01",
        "auto_renew": True,
        "annual_value": 150000.00,
        "payment_terms": "net_30",
        "products": ["platform_enterprise", "analytics_pro"],
        "discount_pct": 8.0,
        "renewal_status": "auto_renew_active",
    },
}


@tool()
def get_contract_details(account_id: str):
    """
    Retrieves contract details for an account including terms, products, and renewal status.

    Args:
        account_id: The unique account identifier (e.g. "A-100").

    Returns:
        Contract details including dates, value, products, discount, and renewal status, or None if not found.
    """
    normalized = str(account_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
