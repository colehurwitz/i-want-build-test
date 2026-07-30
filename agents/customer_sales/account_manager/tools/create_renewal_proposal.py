from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("a-100", "expansion"): {
        "proposal_id": "PROP-3001",
        "account_id": "A-100",
        "proposal_type": "expansion",
        "status": "draft",
        "proposed_arr": 300000.00,
        "discount_pct": 12.0,
        "valid_until": "2024-04-30",
        "items": ["automation_suite_upgrade", "additional_50_seats"],
    },
    ("a-200", "retention"): {
        "proposal_id": "PROP-3002",
        "account_id": "A-200",
        "proposal_type": "retention",
        "status": "draft",
        "proposed_arr": 160000.00,
        "discount_pct": 15.0,
        "valid_until": "2024-04-30",
        "items": ["custom_pricing_package", "dedicated_csm", "quarterly_health_checks"],
    },
    ("a-300", "retention"): {
        "proposal_id": "PROP-3003",
        "account_id": "A-300",
        "proposal_type": "retention",
        "status": "draft",
        "proposed_arr": 70000.00,
        "discount_pct": 10.0,
        "valid_until": "2024-04-30",
        "items": ["usage_review_sessions", "training_credits"],
    },
    ("a-500", "expansion"): {
        "proposal_id": "PROP-3004",
        "account_id": "A-500",
        "proposal_type": "expansion",
        "status": "draft",
        "proposed_arr": 200000.00,
        "discount_pct": 10.0,
        "valid_until": "2024-04-30",
        "items": ["additional_seats", "automation_suite", "premium_support"],
    },
}


@tool()
def create_renewal_proposal(account_id: str, proposal_type: str, adjustments: dict):
    """
    Creates a renewal or expansion proposal for an account.

    Args:
        account_id: The unique account identifier (e.g. "A-100").
        proposal_type: The type of proposal ("renewal", "expansion", "retention", "upsell").
        adjustments: A dictionary of proposed adjustments (e.g. {"discount_pct": 10, "additional_seats": 50}).

    Returns:
        Proposal details including proposal_id, proposed ARR, discount, and items, or None if creation failed.
    """
    key = (
        str(account_id).lower().strip(),
        str(proposal_type).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
