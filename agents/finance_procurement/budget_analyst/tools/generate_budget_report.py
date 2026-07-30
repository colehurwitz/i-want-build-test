from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("engineering", True): {
        "report_id": "RPT-5001",
        "department": "Engineering",
        "summary": "Engineering is at 60% budget utilization with 6 months remaining. Spending is on track with cloud infrastructure being the largest non-salary expense.",
        "recommendations": [
            "Consider renegotiating cloud hosting contract — current spend is 17.8% of quarterly budget",
            "Training budget is underutilized at 2.2% — consider allocating more for team development",
            "Forecast shows budget will be nearly fully spent by year end with $50K remaining",
        ],
        "forecast_included": True,
        "generated_at": "2024-06-15",
    },
    ("engineering", False): {
        "report_id": "RPT-5002",
        "department": "Engineering",
        "summary": "Engineering is at 60% budget utilization. Spending is on track with $800K remaining.",
        "recommendations": [
            "Cloud infrastructure spending is the largest non-salary category",
            "Training budget is underutilized",
        ],
        "forecast_included": False,
        "generated_at": "2024-06-15",
    },
    ("marketing", True): {
        "report_id": "RPT-5003",
        "department": "Marketing",
        "summary": "ALERT: Marketing is at 96.7% budget utilization with only $50K remaining. Forecast shows budget will be exceeded by $180K.",
        "recommendations": [
            "URGENT: Reduce advertising spend immediately — currently 50% of quarterly budget",
            "Events budget at 24% is high — consider virtual alternatives for remaining quarter",
            "Request emergency budget reallocation of at least $180K to cover projected shortfall",
        ],
        "forecast_included": True,
        "generated_at": "2024-06-15",
    },
    ("sales", True): {
        "report_id": "RPT-5004",
        "department": "Sales",
        "summary": "Sales is at 50% budget utilization — well under budget with $900K remaining. No immediate concerns.",
        "recommendations": [
            "Travel budget at 20% is the second largest category — monitor for Q3 conference season",
            "Budget surplus could be reallocated to departments in need",
            "Forecast shows $450K will remain at year end — consider investment opportunities",
        ],
        "forecast_included": True,
        "generated_at": "2024-06-15",
    },
}


@tool()
def generate_budget_report(department: str, include_forecast: bool):
    """
    Generates a comprehensive budget report for a department.

    Args:
        department: The department name (e.g. "Engineering").
        include_forecast: Whether to include spending forecast projections in the report.

    Returns:
        Report including report_id, summary, recommendations list, and whether forecast was included, or None if generation failed.
    """
    key = (
        str(department).lower().strip(),
        bool(include_forecast),
    )
    return STUB_RESPONSES.get(key)
