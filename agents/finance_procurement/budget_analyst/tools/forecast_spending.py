from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("engineering", 6): {
        "department": "Engineering",
        "months_ahead": 6,
        "projected_spend": 1950000.00,
        "projected_remaining": 50000.00,
        "burn_rate": 125000.00,
        "will_exceed": False,
        "confidence": 0.85,
        "methodology": "linear_trend",
    },
    ("marketing", 6): {
        "department": "Marketing",
        "months_ahead": 6,
        "projected_spend": 1680000.00,
        "projected_remaining": -180000.00,
        "burn_rate": 166667.00,
        "will_exceed": True,
        "confidence": 0.90,
        "methodology": "linear_trend",
    },
    ("sales", 6): {
        "department": "Sales",
        "months_ahead": 6,
        "projected_spend": 1350000.00,
        "projected_remaining": 450000.00,
        "burn_rate": 150000.00,
        "will_exceed": False,
        "confidence": 0.80,
        "methodology": "linear_trend",
    },
}


@tool()
def forecast_spending(department: str, months_ahead: int):
    """
    Projects future spending for a department based on current trends.

    Args:
        department: The department name (e.g. "Engineering").
        months_ahead: Number of months to forecast (1-12).

    Returns:
        Forecast including projected_spend, projected_remaining, burn_rate, will_exceed flag, and confidence level, or None if department not found.
    """
    key = (
        str(department).lower().strip(),
        int(months_ahead),
    )
    return STUB_RESPONSES.get(key)
