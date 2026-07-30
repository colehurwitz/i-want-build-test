from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("exp-1001", "emp-500"): {
        "status": "submitted",
        "approval_deadline": "2024-03-22",
        "approver_name": "Karen Wu",
    },
    ("exp-1002", "emp-501"): {
        "status": "submitted",
        "approval_deadline": "2024-03-22",
        "approver_name": "Rachel Kim",
    },
    ("exp-1003", "emp-502"): {
        "status": "submitted",
        "approval_deadline": "2024-03-22",
        "approver_name": "Tom Harris",
    },
    ("exp-1004", "emp-502"): {
        "status": "submitted",
        "approval_deadline": "2024-03-22",
        "approver_name": "Tom Harris",
    },
    ("exp-1005", "emp-900"): {
        "status": "submitted",
        "approval_deadline": "2024-03-22",
        "approver_name": "VP Finance",
    },
}


@tool()
def submit_for_approval(report_id: str, approver_id: str):
    """
    Submits an expense report for managerial approval.

    Args:
        report_id: The expense report ID (e.g. "EXP-1001").
        approver_id: The approver's employee ID, typically the employee's manager.

    Returns:
        Submission status including approval deadline and approver name, or None if submission failed.
    """
    key = (
        str(report_id).lower().strip(),
        str(approver_id).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
