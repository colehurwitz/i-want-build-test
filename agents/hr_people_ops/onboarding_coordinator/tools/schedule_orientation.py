from ibm_watsonx_orchestrate.agent_builder.tools import tool
from typing import List

STUB_RESPONSES = {
    "e-500": {
        "employee_id": "E-500",
        "scheduled": [
            {"session": "Company Overview", "date": "2024-08-01", "time": "09:00-10:30"},
            {"session": "IT Setup", "date": "2024-08-01", "time": "11:00-12:00"},
            {"session": "Security Training", "date": "2024-08-01", "time": "13:00-14:30"},
            {"session": "Department Introduction", "date": "2024-08-02", "time": "09:00-10:30"},
            {"session": "Team Meet", "date": "2024-08-02", "time": "11:00-12:00"},
            {"session": "Role-Specific Training", "date": "2024-08-05", "time": "09:00-12:00"},
        ],
        "status": "confirmed",
    },
    "e-501": {
        "employee_id": "E-501",
        "scheduled": [
            {"session": "Company Overview", "date": "2024-09-02", "time": "09:00-10:30"},
            {"session": "IT Setup", "date": "2024-09-02", "time": "11:00-12:00"},
            {"session": "Security Training", "date": "2024-09-02", "time": "13:00-14:30"},
            {"session": "Department Introduction", "date": "2024-09-03", "time": "09:00-10:30"},
            {"session": "Team Meet", "date": "2024-09-03", "time": "11:00-12:00"},
            {"session": "Sales Methodology Training", "date": "2024-09-04", "time": "09:00-12:00"},
        ],
        "status": "confirmed",
    },
    "e-502": {
        "employee_id": "E-502",
        "scheduled": [
            {"session": "Company Overview", "date": "2024-08-05", "time": "09:00-10:30"},
            {"session": "IT Setup", "date": "2024-08-05", "time": "11:00-12:00"},
            {"session": "Security Training", "date": "2024-08-05", "time": "13:00-14:30"},
            {"session": "Department Introduction", "date": "2024-08-06", "time": "09:00-10:30"},
            {"session": "Team Meet", "date": "2024-08-06", "time": "11:00-12:00"},
            {"session": "Leadership Training", "date": "2024-08-07", "time": "09:00-12:00"},
        ],
        "status": "confirmed",
        "note": "Start date 2024-08-03 is a Saturday. Orientation sessions scheduled starting Monday 2024-08-05.",
    },
    "e-503": {
        "employee_id": "E-503",
        "scheduled": [
            {"session": "Company Overview", "date": "2024-10-01", "time": "09:00-10:30"},
            {"session": "IT Setup", "date": "2024-10-01", "time": "11:00-12:00"},
            {"session": "Security Training", "date": "2024-10-01", "time": "13:00-14:30"},
            {"session": "Department Introduction", "date": "2024-10-02", "time": "09:00-10:30"},
            {"session": "Team Meet", "date": "2024-10-02", "time": "11:00-12:00"},
            {"session": "Role-Specific Training", "date": "2024-10-03", "time": "09:00-12:00"},
        ],
        "status": "confirmed",
    },
    "e-504": {
        "employee_id": "E-504",
        "scheduled": [
            {"session": "Company Overview", "date": "2024-10-01", "time": "09:00-10:30"},
            {"session": "IT Setup", "date": "2024-10-01", "time": "11:00-12:00"},
            {"session": "Security Training", "date": "2024-10-01", "time": "13:00-14:30"},
            {"session": "Department Introduction", "date": "2024-10-02", "time": "09:00-10:30"},
            {"session": "Team Meet", "date": "2024-10-02", "time": "11:00-12:00"},
            {"session": "Role-Specific Training", "date": "2024-10-03", "time": "09:00-12:00"},
        ],
        "status": "confirmed",
    },
}


@tool()
def schedule_orientation(employee_id: str, start_date: str, sessions: list):
    """
    Schedules orientation sessions for a new employee.

    Args:
        employee_id: The new employee's ID (e.g. "E-500").
        start_date: The employee's start date in YYYY-MM-DD format.
        sessions: List of session names to schedule (e.g. ["Company Overview", "IT Setup", "Security Training"]).

    Returns:
        The scheduled sessions with dates and times, or None if scheduling failed.
    """
    normalized = str(employee_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
