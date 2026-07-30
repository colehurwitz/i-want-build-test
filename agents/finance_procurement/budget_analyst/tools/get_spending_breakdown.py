from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("engineering", "q2"): {
        "department": "Engineering",
        "period": "Q2 2024",
        "total_spent": 450000.00,
        "categories": [
            {"name": "Salaries", "amount": 300000.00, "percentage": 66.7},
            {"name": "Cloud Infrastructure", "amount": 80000.00, "percentage": 17.8},
            {"name": "Software Licenses", "amount": 40000.00, "percentage": 8.9},
            {"name": "Equipment", "amount": 20000.00, "percentage": 4.4},
            {"name": "Training", "amount": 10000.00, "percentage": 2.2},
        ],
    },
    ("marketing", "q2"): {
        "department": "Marketing",
        "period": "Q2 2024",
        "total_spent": 500000.00,
        "categories": [
            {"name": "Advertising", "amount": 250000.00, "percentage": 50.0},
            {"name": "Events", "amount": 120000.00, "percentage": 24.0},
            {"name": "Salaries", "amount": 100000.00, "percentage": 20.0},
            {"name": "Software Tools", "amount": 30000.00, "percentage": 6.0},
        ],
    },
    ("sales", "q2"): {
        "department": "Sales",
        "period": "Q2 2024",
        "total_spent": 300000.00,
        "categories": [
            {"name": "Salaries & Commissions", "amount": 200000.00, "percentage": 66.7},
            {"name": "Travel", "amount": 60000.00, "percentage": 20.0},
            {"name": "CRM Software", "amount": 25000.00, "percentage": 8.3},
            {"name": "Conferences", "amount": 15000.00, "percentage": 5.0},
        ],
    },
}


@tool()
def get_spending_breakdown(department: str, period: str):
    """
    Gets a detailed spending breakdown by category for a department and time period.

    Args:
        department: The department name (e.g. "Engineering").
        period: The time period to analyze (e.g. "Q1", "Q2", "H1", "YTD").

    Returns:
        Spending breakdown including total_spent and categories list with amounts and percentages, or None if not found.
    """
    key = (
        str(department).lower().strip(),
        str(period).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
