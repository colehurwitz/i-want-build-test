from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("v-300", "price_escalation", "cpi + 1.5%"): {
        "vendor_id": "V-300",
        "negotiation_id": "NEG-300",
        "proposed_change": "price_escalation",
        "current_value": "Fixed pricing",
        "proposed_value": "CPI + 1.5%",
        "vendor_response": "accepted",
        "notes": "Vendor agreed to move from fixed to CPI-linked pricing at CPI + 1.5%",
    },
    ("v-300", "volume_discount", "3% on orders > $20,000"): {
        "vendor_id": "V-300",
        "negotiation_id": "NEG-301",
        "proposed_change": "volume_discount",
        "current_value": "None",
        "proposed_value": "3% on orders > $20,000",
        "vendor_response": "counter_offer",
        "counter_value": "2% on orders > $25,000",
        "notes": "Vendor willing to offer discount but at higher threshold",
    },
    ("v-200", "payment_terms", "net-60"): {
        "vendor_id": "V-200",
        "negotiation_id": "NEG-200",
        "proposed_change": "payment_terms",
        "current_value": "Net-30",
        "proposed_value": "Net-60",
        "vendor_response": "rejected",
        "notes": "Vendor requires Net-30 minimum due to cash flow constraints",
    },
    ("v-200", "performance_penalties", "true"): {
        "vendor_id": "V-200",
        "negotiation_id": "NEG-201",
        "proposed_change": "performance_penalties",
        "current_value": "False",
        "proposed_value": "True",
        "vendor_response": "accepted",
        "notes": "Vendor agrees to include performance penalty clauses for late delivery and quality failures",
    },
}


@tool()
def negotiate_terms(vendor_id: str, proposed_changes: dict):
    """
    Proposes contract term changes to a vendor and gets their response.

    Args:
        vendor_id: The vendor identifier (e.g. "V-300").
        proposed_changes: Dictionary with the term to change and proposed value (e.g. {"term": "price_escalation", "value": "CPI + 1.5%"}).

    Returns:
        Negotiation result with vendor response (accepted/rejected/counter_offer), or None if negotiation failed.
    """
    term = str(proposed_changes.get("term", "")).lower().strip()
    value = str(proposed_changes.get("value", "")).lower().strip()
    key = (
        str(vendor_id).lower().strip(),
        term,
        value,
    )
    return STUB_RESPONSES.get(key)
