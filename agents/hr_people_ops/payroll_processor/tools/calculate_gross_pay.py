from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("e-100", 80.0, 5.0): {
        "employee_id": "E-100",
        "base_rate": 50.00,
        "regular_hours": 80.0,
        "regular_pay": 4000.00,
        "overtime_rate": 75.00,
        "overtime_hours": 5.0,
        "overtime_pay": 375.00,
        "gross_total": 4375.00,
    },
    ("e-100", 80.0, 0.0): {
        "employee_id": "E-100",
        "base_rate": 50.00,
        "regular_hours": 80.0,
        "regular_pay": 4000.00,
        "overtime_rate": 75.00,
        "overtime_hours": 0.0,
        "overtime_pay": 0.00,
        "gross_total": 4000.00,
    },
    ("e-101", 80.0, 10.0): {
        "employee_id": "E-101",
        "base_rate": 42.50,
        "regular_hours": 80.0,
        "regular_pay": 3400.00,
        "overtime_rate": 63.75,
        "overtime_hours": 10.0,
        "overtime_pay": 637.50,
        "gross_total": 4037.50,
    },
    ("e-102", 80.0, 0.0): {
        "employee_id": "E-102",
        "base_rate": 55.00,
        "regular_hours": 80.0,
        "regular_pay": 4400.00,
        "overtime_rate": 82.50,
        "overtime_hours": 0.0,
        "overtime_pay": 0.00,
        "gross_total": 4400.00,
    },
}


@tool()
def calculate_gross_pay(employee_id: str, hours: float, overtime_hours: float):
    """
    Calculates an employee's gross pay for a given number of regular and overtime hours.

    Args:
        employee_id: The employee's ID (e.g. "E-100").
        hours: The number of regular hours worked.
        overtime_hours: The number of overtime hours worked.

    Returns:
        The pay calculation breakdown including base rate, regular pay, overtime rate, overtime pay, and gross total, or None if the employee is not found.
    """
    key = (
        str(employee_id).lower().strip(),
        float(hours),
        float(overtime_hours),
    )
    return STUB_RESPONSES.get(key)
