from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("e-500", "t-003", "completed"): {
        "status": "updated",
        "employee_id": "E-500",
        "task_id": "T-003",
        "task_name": "Buddy Assignment",
        "new_status": "completed",
        "updated_at": "2024-07-20",
    },
    ("e-500", "t-004", "completed"): {
        "status": "updated",
        "employee_id": "E-500",
        "task_id": "T-004",
        "task_name": "Orientation Scheduling",
        "new_status": "completed",
        "updated_at": "2024-07-20",
    },
    ("e-500", "t-005", "completed"): {
        "status": "updated",
        "employee_id": "E-500",
        "task_id": "T-005",
        "task_name": "Equipment Delivery",
        "new_status": "completed",
        "updated_at": "2024-07-21",
    },
    ("e-501", "t-012", "completed"): {
        "status": "updated",
        "employee_id": "E-501",
        "task_id": "T-012",
        "task_name": "Account Provisioning",
        "new_status": "completed",
        "updated_at": "2024-08-21",
    },
    ("e-501", "t-013", "blocked"): {
        "status": "updated",
        "employee_id": "E-501",
        "task_id": "T-013",
        "task_name": "Buddy Assignment",
        "new_status": "blocked",
        "updated_at": "2024-08-21",
        "blocker": "No eligible buddies in Sales department",
    },
}


@tool()
def update_onboarding_task(employee_id: str, task_id: str, status: str, notes: str):
    """
    Updates the status of an onboarding task for an employee.

    Args:
        employee_id: The employee's ID (e.g. "E-500").
        task_id: The task ID to update (e.g. "T-003"), from the onboarding checklist.
        status: The new status for the task ("pending", "in_progress", "completed", "blocked").
        notes: Notes or comments about the task update.

    Returns:
        The update result with the new status and timestamp, or None if the task was not found.
    """
    key = (
        str(employee_id).lower().strip(),
        str(task_id).lower().strip(),
        str(status).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
