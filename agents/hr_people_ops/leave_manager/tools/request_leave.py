from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("e-100", "annual", "2024-12-23", "2024-12-27"): {
        "request_id": "LR-001",
        "status": "pending_approval",
        "employee_id": "E-100",
        "leave_type": "annual",
        "start_date": "2024-12-23",
        "end_date": "2024-12-27",
        "days_requested": 5,
        "submitted_date": "2024-12-01",
    },
    ("e-101", "annual", "2024-11-18", "2024-11-20"): {
        "request_id": "LR-002",
        "status": "pending_approval",
        "employee_id": "E-101",
        "leave_type": "annual",
        "start_date": "2024-11-18",
        "end_date": "2024-11-20",
        "days_requested": 3,
        "submitted_date": "2024-11-10",
    },
    ("e-102", "sick", "2024-11-12", "2024-11-12"): {
        "request_id": "LR-003",
        "status": "pending_approval",
        "employee_id": "E-102",
        "leave_type": "sick",
        "start_date": "2024-11-12",
        "end_date": "2024-11-12",
        "days_requested": 1,
        "submitted_date": "2024-11-11",
    },
    ("e-101", "personal", "2024-11-22", "2024-11-25"): {
        "request_id": "LR-005",
        "status": "pending_approval",
        "employee_id": "E-101",
        "leave_type": "personal",
        "start_date": "2024-11-22",
        "end_date": "2024-11-25",
        "days_requested": 2,
        "submitted_date": "2024-11-15",
    },
}


@tool()
def request_leave(employee_id: str, leave_type: str, start_date: str, end_date: str, reason: str):
    """
    Submits a leave request for an employee.

    Args:
        employee_id: The employee's ID (e.g. "E-100").
        leave_type: The type of leave (e.g. "annual", "sick", "personal", "parental", "unpaid").
        start_date: The start date of the leave in YYYY-MM-DD format.
        end_date: The end date of the leave in YYYY-MM-DD format.
        reason: The reason for the leave request.

    Returns:
        The leave request details including request ID and status, or None if submission failed.
    """
    key = (
        str(employee_id).lower().strip(),
        str(leave_type).lower().strip(),
        str(start_date).strip(),
        str(end_date).strip(),
    )
    return STUB_RESPONSES.get(key)
