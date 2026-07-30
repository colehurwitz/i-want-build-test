from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "travel": {
        "max_single_amount": 2000.00,
        "requires_receipt_above": 75.00,
        "requires_preapproval_above": 1000.00,
        "allowed_vendors": ["any"],
        "policy_notes": "International travel requires VP pre-approval.",
    },
    "meals": {
        "max_single_amount": 150.00,
        "requires_receipt_above": 25.00,
        "requires_preapproval_above": 100.00,
        "allowed_vendors": ["any"],
        "policy_notes": "Team meals over $100 need manager pre-approval.",
    },
    "office_supplies": {
        "max_single_amount": 500.00,
        "requires_receipt_above": 50.00,
        "requires_preapproval_above": 250.00,
        "allowed_vendors": ["OfficeMax", "Staples", "Amazon Business"],
        "policy_notes": "Must use approved vendor list.",
    },
    "equipment": {
        "max_single_amount": 5000.00,
        "requires_receipt_above": 0.01,
        "requires_preapproval_above": 1500.00,
        "allowed_vendors": ["Dell", "Apple", "Lenovo", "HP"],
        "policy_notes": "All equipment purchases require receipt regardless of amount.",
    },
    "training": {
        "max_single_amount": 3000.00,
        "requires_receipt_above": 50.00,
        "requires_preapproval_above": 500.00,
        "allowed_vendors": ["any"],
        "policy_notes": "Conference attendance requires manager approval.",
    },
}


@tool()
def get_expense_policy(category: str):
    """
    Retrieves the expense policy rules for a specific category.

    Args:
        category: The expense category ("travel", "meals", "office_supplies", "equipment", "training").

    Returns:
        Policy details including max_single_amount, receipt requirements, preapproval thresholds, and allowed vendors, or None if category not found.
    """
    normalized = str(category).lower().strip()
    return STUB_RESPONSES.get(normalized)
