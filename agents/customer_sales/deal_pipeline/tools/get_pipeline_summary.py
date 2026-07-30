from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("sr-100", "q3"): {
        "owner_id": "SR-100",
        "quarter": "Q3",
        "total_deals": 3,
        "total_value": 240000.00,
        "weighted_value": 112500.00,
        "deals": [
            {"deal_id": "D-100", "title": "Acme Enterprise License", "value": 75000.00, "stage": "qualification", "probability": 0.25},
            {"deal_id": "D-200", "title": "GlobalTech Platform Migration", "value": 120000.00, "stage": "negotiation", "probability": 0.75},
            {"deal_id": "D-500", "title": "FinServ Compliance Module", "value": 45000.00, "stage": "qualification", "probability": 0.25},
        ],
        "quota": 300000.00,
        "attainment_pct": 37.5,
    },
    ("sr-200", "q3"): {
        "owner_id": "SR-200",
        "quarter": "Q3",
        "total_deals": 2,
        "total_value": 215000.00,
        "weighted_value": 101500.00,
        "deals": [
            {"deal_id": "D-300", "title": "StartupXYZ Starter Package", "value": 15000.00, "stage": "prospecting", "probability": 0.10},
            {"deal_id": "D-400", "title": "MegaRetail Analytics Suite", "value": 200000.00, "stage": "proposal", "probability": 0.50},
        ],
        "quota": 250000.00,
        "attainment_pct": 40.6,
    },
    ("sr-100", "q4"): {
        "owner_id": "SR-100",
        "quarter": "Q4",
        "total_deals": 2,
        "total_value": 195000.00,
        "weighted_value": 78750.00,
        "deals": [
            {"deal_id": "D-100", "title": "Acme Enterprise License", "value": 75000.00, "stage": "proposal", "probability": 0.50},
            {"deal_id": "D-200", "title": "GlobalTech Platform Migration", "value": 120000.00, "stage": "closed_won", "probability": 1.00},
        ],
        "quota": 300000.00,
        "attainment_pct": 26.25,
    },
}


@tool()
def get_pipeline_summary(owner_id: str, quarter: str):
    """
    Retrieves a summary of a sales rep's deal pipeline for a given quarter.

    Args:
        owner_id: The sales rep's ID (e.g. "SR-100").
        quarter: The fiscal quarter (e.g. "Q3", "Q4").

    Returns:
        Pipeline summary including deal list, total value, weighted value, quota, and attainment percentage, or None if not found.
    """
    key = (
        str(owner_id).lower().strip(),
        str(quarter).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
