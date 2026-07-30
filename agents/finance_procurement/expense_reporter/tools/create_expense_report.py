from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("emp-100", "business trip travel expenses", 450.0, "travel", True): {
        "report_id": "EXP-1001",
        "status": "draft",
        "created_at": "2024-03-15",
        "total_amount": 450.00,
    },
    ("emp-101", "team lunch", 25.0, "meals", False): {
        "report_id": "EXP-1002",
        "status": "draft",
        "created_at": "2024-03-15",
        "total_amount": 25.00,
    },
    ("emp-102", "office supplies", 200.0, "office_supplies", False): {
        "report_id": "EXP-1003",
        "status": "draft",
        "created_at": "2024-03-15",
        "total_amount": 200.00,
    },
    ("emp-102", "conference registration", 1500.0, "training", True): {
        "report_id": "EXP-1004",
        "status": "draft",
        "created_at": "2024-03-15",
        "total_amount": 1500.00,
    },
    ("emp-500", "new monitor for team lead", 3000.0, "equipment", True): {
        "report_id": "EXP-1005",
        "status": "draft",
        "created_at": "2024-03-15",
        "total_amount": 3000.00,
    },
}


@tool()
def create_expense_report(employee_id: str, title: str, amount: float, category: str, receipt_attached: bool):
    """
    Creates a new expense report for an employee.

    Args:
        employee_id: The employee's ID (e.g. "EMP-100").
        title: A descriptive title for the expense report.
        amount: The total expense amount in USD.
        category: The expense category ("travel", "meals", "office_supplies", "equipment", "training", "other").
        receipt_attached: Whether a receipt is attached to this expense.

    Returns:
        The created expense report details including report_id and status, or None if creation failed.
    """
    key = (
        str(employee_id).lower().strip(),
        str(title).lower().strip(),
        float(amount),
        str(category).lower().strip(),
        bool(receipt_attached),
    )
    return STUB_RESPONSES.get(key)
