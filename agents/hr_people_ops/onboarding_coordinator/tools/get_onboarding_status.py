from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "e-500": {
        "employee_id": "E-500",
        "name": "Alex Turner",
        "status": "in_progress",
        "start_date": "2024-08-01",
        "completed_tasks": [
            {"task_id": "T-001", "name": "IT Setup", "completed_date": "2024-07-18"},
            {"task_id": "T-002", "name": "Account Provisioning", "completed_date": "2024-07-19"},
        ],
        "pending_tasks": [
            {"task_id": "T-003", "name": "Buddy Assignment", "status": "pending"},
            {"task_id": "T-004", "name": "Orientation Scheduling", "status": "pending"},
            {"task_id": "T-005", "name": "Equipment Delivery", "status": "pending"},
        ],
        "progress_pct": 40,
    },
    "e-501": {
        "employee_id": "E-501",
        "name": "Sam Lee",
        "status": "in_progress",
        "start_date": "2024-09-01",
        "completed_tasks": [
            {"task_id": "T-011", "name": "IT Setup", "completed_date": "2024-08-20"},
        ],
        "pending_tasks": [
            {"task_id": "T-012", "name": "Account Provisioning", "status": "pending"},
            {"task_id": "T-013", "name": "Buddy Assignment", "status": "pending"},
            {"task_id": "T-014", "name": "Orientation Scheduling", "status": "pending"},
            {"task_id": "T-015", "name": "Equipment Delivery", "status": "pending"},
        ],
        "progress_pct": 20,
    },
    "e-502": {
        "employee_id": "E-502",
        "name": "Jordan Park",
        "status": "not_started",
        "start_date": "2024-08-03",
        "completed_tasks": [],
        "pending_tasks": [
            {"task_id": "T-021", "name": "IT Setup", "status": "pending"},
            {"task_id": "T-022", "name": "Account Provisioning", "status": "pending"},
            {"task_id": "T-023", "name": "Buddy Assignment", "status": "pending"},
            {"task_id": "T-024", "name": "Orientation Scheduling", "status": "pending"},
            {"task_id": "T-025", "name": "Equipment Delivery", "status": "pending"},
            {"task_id": "T-026", "name": "Manager Access Setup", "status": "pending"},
        ],
        "progress_pct": 0,
    },
}


@tool()
def get_onboarding_status(employee_id: str):
    """
    Gets the current onboarding status for a new employee.

    Args:
        employee_id: The employee's ID (e.g. "E-500").

    Returns:
        The onboarding status with completed and pending tasks, progress percentage, and start date, or None if not found.
    """
    normalized = str(employee_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
