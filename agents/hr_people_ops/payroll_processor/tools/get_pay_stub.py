from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("e-100", "2024-01"): {
        "employee_id": "E-100",
        "period": "2024-01",
        "gross_pay": 8500.00,
        "deductions": {
            "federal_tax": 1700.00,
            "state_tax": 680.00,
            "health_insurance": 450.00,
            "retirement_401k": 510.00,
        },
        "net_pay": 5160.00,
        "pay_date": "2024-01-31",
    },
    ("e-100", "2024-02"): {
        "employee_id": "E-100",
        "period": "2024-02",
        "gross_pay": 8500.00,
        "deductions": {
            "federal_tax": 1700.00,
            "state_tax": 680.00,
            "health_insurance": 450.00,
            "retirement_401k": 510.00,
        },
        "net_pay": 5160.00,
        "pay_date": "2024-02-29",
    },
    ("e-101", "2024-01"): {
        "employee_id": "E-101",
        "period": "2024-01",
        "gross_pay": 7200.00,
        "deductions": {
            "federal_tax": 1296.00,
            "state_tax": 576.00,
            "health_insurance": 350.00,
            "retirement_401k": 432.00,
        },
        "net_pay": 4546.00,
        "pay_date": "2024-01-31",
    },
    ("e-102", "2024-01"): {
        "employee_id": "E-102",
        "period": "2024-01",
        "gross_pay": 9500.00,
        "deductions": {
            "federal_tax": 2090.00,
            "state_tax": 760.00,
            "health_insurance": 550.00,
            "retirement_401k": 570.00,
        },
        "net_pay": 5530.00,
        "pay_date": "2024-01-31",
    },
}


@tool()
def get_pay_stub(employee_id: str, period: str):
    """
    Gets an employee's pay stub for a specific pay period.

    Args:
        employee_id: The employee's ID (e.g. "E-100").
        period: The pay period in YYYY-MM format (e.g. "2024-01").

    Returns:
        The pay stub with gross pay, itemized deductions, net pay, and pay date, or None if not found.
    """
    key = (
        str(employee_id).lower().strip(),
        str(period).strip(),
    )
    return STUB_RESPONSES.get(key)
