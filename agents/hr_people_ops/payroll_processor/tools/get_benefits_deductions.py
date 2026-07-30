from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "e-100": {
        "employee_id": "E-100",
        "health_plan": "PPO Gold",
        "health_monthly": 450.00,
        "dental_monthly": 45.00,
        "vision_monthly": 15.00,
        "retirement_401k_pct": 6.0,
        "retirement_match_pct": 4.0,
        "life_insurance_monthly": 25.00,
        "total_monthly_deductions": 535.00,
    },
    "e-101": {
        "employee_id": "E-101",
        "health_plan": "HMO Basic",
        "health_monthly": 350.00,
        "dental_monthly": 35.00,
        "vision_monthly": 12.00,
        "retirement_401k_pct": 6.0,
        "retirement_match_pct": 3.0,
        "life_insurance_monthly": 20.00,
        "total_monthly_deductions": 417.00,
    },
    "e-102": {
        "employee_id": "E-102",
        "health_plan": "PPO Platinum",
        "health_monthly": 550.00,
        "dental_monthly": 55.00,
        "vision_monthly": 18.00,
        "retirement_401k_pct": 8.0,
        "retirement_match_pct": 5.0,
        "life_insurance_monthly": 30.00,
        "total_monthly_deductions": 653.00,
    },
}


@tool()
def get_benefits_deductions(employee_id: str):
    """
    Gets an employee's current benefits and deductions summary.

    Args:
        employee_id: The employee's ID (e.g. "E-100").

    Returns:
        The benefits details including health plan, dental, vision, retirement, and life insurance deductions, or None if not found.
    """
    normalized = str(employee_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
