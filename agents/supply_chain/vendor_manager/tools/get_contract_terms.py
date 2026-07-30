from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "v-100": {
        "vendor_id": "V-100",
        "contract_id": "CTR-100",
        "start_date": "2024-01-01",
        "end_date": "2026-12-31",
        "auto_renewal": True,
        "cancellation_notice_days": 90,
        "payment_terms": "Net-30",
        "price_escalation": "CPI + 1.5%",
        "volume_discount": "5% on orders > $50,000",
        "performance_penalties": True,
        "minimum_order": 5000.00,
        "status": "active",
    },
    "v-200": {
        "vendor_id": "V-200",
        "contract_id": "CTR-200",
        "start_date": "2024-06-01",
        "end_date": "2026-05-31",
        "auto_renewal": True,
        "cancellation_notice_days": 60,
        "payment_terms": "Net-30",
        "price_escalation": "CPI + 2%",
        "volume_discount": "3% on orders > $25,000",
        "performance_penalties": False,
        "minimum_order": 10000.00,
        "status": "expired",
    },
    "v-300": {
        "vendor_id": "V-300",
        "contract_id": "CTR-300",
        "start_date": "2025-01-01",
        "end_date": "2026-12-31",
        "auto_renewal": False,
        "cancellation_notice_days": 30,
        "payment_terms": "Net-30",
        "price_escalation": "Fixed pricing",
        "volume_discount": "None",
        "performance_penalties": True,
        "minimum_order": 2000.00,
        "status": "active",
    },
    "v-400": {
        "vendor_id": "V-400",
        "contract_id": "CTR-400",
        "start_date": "2025-03-01",
        "end_date": "2027-02-28",
        "auto_renewal": True,
        "cancellation_notice_days": 90,
        "payment_terms": "Net-30",
        "price_escalation": "CPI + 2%",
        "volume_discount": "4% on orders > $30,000",
        "performance_penalties": True,
        "minimum_order": 5000.00,
        "status": "active",
    },
    "v-500": {
        "vendor_id": "V-500",
        "contract_id": "CTR-500",
        "start_date": "2025-06-01",
        "end_date": "2026-05-31",
        "auto_renewal": False,
        "cancellation_notice_days": 30,
        "payment_terms": "Net-15",
        "price_escalation": "CPI + 3%",
        "volume_discount": "None",
        "performance_penalties": False,
        "minimum_order": 1000.00,
        "status": "expired",
    },
}


@tool()
def get_contract_terms(vendor_id: str):
    """
    Retrieves the current contract terms for a vendor.

    Args:
        vendor_id: The vendor identifier (e.g. "V-100").

    Returns:
        Contract details including dates, payment terms, pricing rules, and status, or None if not found.
    """
    normalized = str(vendor_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
