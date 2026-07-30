from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("e-500", "2024-08-01", "engineering", "software engineer"): {
        "checklist_id": "CL-001",
        "employee_id": "E-500",
        "start_date": "2024-08-01",
        "department": "Engineering",
        "role": "Software Engineer",
        "tasks": [
            {"task_id": "T-001", "name": "IT Setup", "status": "pending"},
            {"task_id": "T-002", "name": "Account Provisioning", "status": "pending"},
            {"task_id": "T-003", "name": "Buddy Assignment", "status": "pending"},
            {"task_id": "T-004", "name": "Orientation Scheduling", "status": "pending"},
            {"task_id": "T-005", "name": "Equipment Delivery", "status": "pending"},
        ],
        "created_date": "2024-07-15",
    },
    ("e-501", "2024-09-01", "sales", "sales representative"): {
        "checklist_id": "CL-002",
        "employee_id": "E-501",
        "start_date": "2024-09-01",
        "department": "Sales",
        "role": "Sales Representative",
        "tasks": [
            {"task_id": "T-011", "name": "IT Setup", "status": "pending"},
            {"task_id": "T-012", "name": "Account Provisioning", "status": "pending"},
            {"task_id": "T-013", "name": "Buddy Assignment", "status": "pending"},
            {"task_id": "T-014", "name": "Orientation Scheduling", "status": "pending"},
            {"task_id": "T-015", "name": "Equipment Delivery", "status": "pending"},
        ],
        "created_date": "2024-08-15",
    },
    ("e-502", "2024-08-03", "engineering", "engineering manager"): {
        "checklist_id": "CL-003",
        "employee_id": "E-502",
        "start_date": "2024-08-03",
        "department": "Engineering",
        "role": "Engineering Manager",
        "tasks": [
            {"task_id": "T-021", "name": "IT Setup", "status": "pending"},
            {"task_id": "T-022", "name": "Account Provisioning", "status": "pending"},
            {"task_id": "T-023", "name": "Buddy Assignment", "status": "pending"},
            {"task_id": "T-024", "name": "Orientation Scheduling", "status": "pending"},
            {"task_id": "T-025", "name": "Equipment Delivery", "status": "pending"},
            {"task_id": "T-026", "name": "Manager Access Setup", "status": "pending"},
        ],
        "created_date": "2024-07-20",
    },
    ("e-503", "2024-10-01", "engineering", "software engineer"): {
        "checklist_id": "CL-004",
        "employee_id": "E-503",
        "start_date": "2024-10-01",
        "department": "Engineering",
        "role": "Software Engineer",
        "tasks": [
            {"task_id": "T-031", "name": "IT Setup", "status": "pending"},
            {"task_id": "T-032", "name": "Account Provisioning", "status": "pending"},
            {"task_id": "T-033", "name": "Buddy Assignment", "status": "pending"},
            {"task_id": "T-034", "name": "Orientation Scheduling", "status": "pending"},
            {"task_id": "T-035", "name": "Equipment Delivery", "status": "pending"},
        ],
        "created_date": "2024-09-15",
    },
    ("e-504", "2024-10-01", "engineering", "software engineer"): {
        "checklist_id": "CL-005",
        "employee_id": "E-504",
        "start_date": "2024-10-01",
        "department": "Engineering",
        "role": "Software Engineer",
        "tasks": [
            {"task_id": "T-041", "name": "IT Setup", "status": "pending"},
            {"task_id": "T-042", "name": "Account Provisioning", "status": "pending"},
            {"task_id": "T-043", "name": "Buddy Assignment", "status": "pending"},
            {"task_id": "T-044", "name": "Orientation Scheduling", "status": "pending"},
            {"task_id": "T-045", "name": "Equipment Delivery", "status": "pending"},
        ],
        "created_date": "2024-09-15",
    },
}


@tool()
def create_onboarding_checklist(employee_id: str, start_date: str, department: str, role: str):
    """
    Creates an onboarding checklist for a new employee based on their role and department.

    Args:
        employee_id: The new employee's ID (e.g. "E-500").
        start_date: The employee's start date in YYYY-MM-DD format.
        department: The department the employee is joining (e.g. "Engineering", "Sales").
        role: The employee's job role (e.g. "Software Engineer").

    Returns:
        The created checklist with task IDs and statuses, or None if creation failed.
    """
    key = (
        str(employee_id).lower().strip(),
        str(start_date).strip(),
        str(department).lower().strip(),
        str(role).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
