from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("e-100", "2024"): [
        {
            "request_id": "LR-100",
            "leave_type": "annual",
            "start_date": "2024-03-15",
            "end_date": "2024-03-20",
            "status": "approved",
            "days": 5,
        },
        {
            "request_id": "LR-101",
            "leave_type": "sick",
            "start_date": "2024-06-10",
            "end_date": "2024-06-11",
            "status": "approved",
            "days": 2,
        },
    ],
    ("e-101", "2024"): [
        {
            "request_id": "LR-110",
            "leave_type": "annual",
            "start_date": "2024-01-02",
            "end_date": "2024-01-05",
            "status": "approved",
            "days": 4,
        },
        {
            "request_id": "LR-111",
            "leave_type": "annual",
            "start_date": "2024-04-10",
            "end_date": "2024-04-19",
            "status": "approved",
            "days": 8,
        },
        {
            "request_id": "LR-112",
            "leave_type": "annual",
            "start_date": "2024-07-01",
            "end_date": "2024-07-05",
            "status": "approved",
            "days": 5,
        },
        {
            "request_id": "LR-113",
            "leave_type": "personal",
            "start_date": "2024-09-15",
            "end_date": "2024-09-15",
            "status": "approved",
            "days": 1,
        },
    ],
    ("e-102", "2024"): [
        {
            "request_id": "LR-120",
            "leave_type": "annual",
            "start_date": "2024-02-12",
            "end_date": "2024-02-16",
            "status": "approved",
            "days": 5,
        },
        {
            "request_id": "LR-121",
            "leave_type": "annual",
            "start_date": "2024-08-05",
            "end_date": "2024-08-09",
            "status": "approved",
            "days": 5,
        },
    ],
    ("e-103", "2024"): [
        {
            "request_id": "LR-130",
            "leave_type": "annual",
            "start_date": "2024-01-15",
            "end_date": "2024-01-19",
            "status": "approved",
            "days": 5,
        },
        {
            "request_id": "LR-131",
            "leave_type": "annual",
            "start_date": "2024-05-20",
            "end_date": "2024-05-24",
            "status": "approved",
            "days": 5,
        },
        {
            "request_id": "LR-132",
            "leave_type": "annual",
            "start_date": "2024-10-07",
            "end_date": "2024-10-08",
            "status": "approved",
            "days": 2,
        },
    ],
}


@tool()
def get_leave_history(employee_id: str, year: str):
    """
    Gets an employee's leave history for a specific year.

    Args:
        employee_id: The employee's ID (e.g. "E-100").
        year: The year to retrieve history for (e.g. "2024").

    Returns:
        A list of past leave requests with their types, dates, status, and duration, or None if no history found.
    """
    key = (
        str(employee_id).lower().strip(),
        str(year).strip(),
    )
    return STUB_RESPONSES.get(key)
