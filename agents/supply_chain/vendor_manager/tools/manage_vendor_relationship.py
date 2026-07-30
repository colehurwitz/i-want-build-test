from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("v-100", "quarterly_review"): {
        "vendor_id": "V-100",
        "action": "quarterly_review",
        "status": "scheduled",
        "details": {
            "meeting_date": "2026-08-15",
            "attendees": ["Procurement Manager", "V-100 Account Rep"],
            "agenda": ["Q2 performance review", "Partnership expansion discussion", "Q3 forecast"],
        },
    },
    ("v-200", "issue_escalation"): {
        "vendor_id": "V-200",
        "action": "issue_escalation",
        "status": "escalated",
        "details": {
            "escalation_id": "ESC-200",
            "issues": ["Declining delivery performance", "Quality defect rate above threshold", "Slow response times"],
            "escalated_to": "VP Supply Chain",
            "deadline": "2026-08-05",
        },
    },
    ("v-300", "contract_renewal"): {
        "vendor_id": "V-300",
        "action": "contract_renewal",
        "status": "initiated",
        "details": {
            "current_contract_end": "2026-12-31",
            "renewal_process_start": "2026-09-01",
            "proposed_term": "2 years",
            "review_items": ["Add volume discounts", "Include performance penalties", "Update pricing terms"],
        },
    },
    ("v-500", "vendor_offboarding"): {
        "vendor_id": "V-500",
        "action": "vendor_offboarding",
        "status": "initiated",
        "details": {
            "offboarding_id": "OFF-500",
            "reason": "Consistently unacceptable performance across all categories",
            "transition_plan": "Shift orders to V-100 and V-300",
            "estimated_completion": "2026-09-30",
            "open_orders_count": 3,
            "action_items": ["Complete pending orders", "Transfer product specs", "Close vendor account"],
        },
    },
    ("v-200", "quarterly_review"): {
        "vendor_id": "V-200",
        "action": "quarterly_review",
        "status": "scheduled",
        "details": {
            "meeting_date": "2026-08-10",
            "attendees": ["Procurement Manager", "V-200 Account Rep", "Quality Manager"],
            "agenda": ["Performance improvement plan review", "Quality corrective actions", "Contract renewal discussion"],
        },
    },
}


@tool()
def manage_vendor_relationship(vendor_id: str, action: str, details: dict):
    """
    Takes a relationship management action for a vendor.

    Args:
        vendor_id: The vendor identifier (e.g. "V-100").
        action: The action to take ("quarterly_review", "issue_escalation", "contract_renewal", "vendor_onboarding", "vendor_offboarding").
        details: Additional details for the action (e.g. {"reason": "declining performance"}).

    Returns:
        Action result with status and details, or None if the action failed.
    """
    key = (
        str(vendor_id).lower().strip(),
        str(action).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
