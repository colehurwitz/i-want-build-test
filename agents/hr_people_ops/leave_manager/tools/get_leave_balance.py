from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("e-100", "annual"): {
        "employee_id": "E-100",
        "leave_type": "annual",
        "balance_days": 15,
        "used_days": 5,
        "pending_days": 2,
        "accrual_rate": 1.25,
    },
    ("e-100", "sick"): {
        "employee_id": "E-100",
        "leave_type": "sick",
        "balance_days": 10,
        "used_days": 2,
        "pending_days": 0,
        "accrual_rate": 0.83,
    },
    ("e-101", "annual"): {
        "employee_id": "E-101",
        "leave_type": "annual",
        "balance_days": 20,
        "used_days": 18,
        "pending_days": 0,
        "accrual_rate": 1.25,
    },
    ("e-101", "personal"): {
        "employee_id": "E-101",
        "leave_type": "personal",
        "balance_days": 3,
        "used_days": 1,
        "pending_days": 0,
        "accrual_rate": 0.25,
    },
    ("e-102", "sick"): {
        "employee_id": "E-102",
        "leave_type": "sick",
        "balance_days": 10,
        "used_days": 0,
        "pending_days": 0,
        "accrual_rate": 0.83,
    },
    ("e-102", "annual"): {
        "employee_id": "E-102",
        "leave_type": "annual",
        "balance_days": 15,
        "used_days": 10,
        "pending_days": 3,
        "accrual_rate": 1.25,
    },
    ("e-103", "annual"): {
        "employee_id": "E-103",
        "leave_type": "annual",
        "balance_days": 12,
        "used_days": 12,
        "pending_days": 0,
        "accrual_rate": 1.0,
    },
    ("e-103", "personal"): {
        "employee_id": "E-103",
        "leave_type": "personal",
        "balance_days": 3,
        "used_days": 0,
        "pending_days": 1,
        "accrual_rate": 0.25,
    },
}


@tool()
def get_leave_balance(employee_id: str, leave_type: str):
    """
    Gets an employee's leave balance for a specific leave type.

    Args:
        employee_id: The employee's ID (e.g. "E-100").
        leave_type: The type of leave (e.g. "annual", "sick", "personal", "parental", "unpaid").

    Returns:
        The leave balance details including total balance, used days, pending days, and accrual rate, or None if not found.
    """
    key = (
        str(employee_id).lower().strip(),
        str(leave_type).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
