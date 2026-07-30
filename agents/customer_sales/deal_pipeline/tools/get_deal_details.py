from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "d-100": {
        "deal_id": "D-100",
        "account_name": "Acme Corp",
        "title": "Acme Enterprise License",
        "value": 75000.00,
        "stage": "qualification",
        "close_probability": 0.25,
        "owner_id": "SR-100",
        "close_date": "2024-06-30",
        "notes": "Initial demo completed, stakeholders identified",
    },
    "d-200": {
        "deal_id": "D-200",
        "account_name": "GlobalTech Inc",
        "title": "GlobalTech Platform Migration",
        "value": 120000.00,
        "stage": "negotiation",
        "close_probability": 0.75,
        "owner_id": "SR-100",
        "close_date": "2024-04-15",
        "notes": "Final contract terms under review",
    },
    "d-300": {
        "deal_id": "D-300",
        "account_name": "StartupXYZ",
        "title": "StartupXYZ Starter Package",
        "value": 15000.00,
        "stage": "prospecting",
        "close_probability": 0.10,
        "owner_id": "SR-200",
        "close_date": "2024-08-30",
        "notes": "Cold outreach, no response yet",
    },
    "d-400": {
        "deal_id": "D-400",
        "account_name": "MegaRetail",
        "title": "MegaRetail Analytics Suite",
        "value": 200000.00,
        "stage": "proposal",
        "close_probability": 0.50,
        "owner_id": "SR-200",
        "close_date": "2024-05-31",
        "notes": "Proposal sent, awaiting feedback from procurement",
    },
    "d-500": {
        "deal_id": "D-500",
        "account_name": "FinServ Partners",
        "title": "FinServ Compliance Module",
        "value": 45000.00,
        "stage": "qualification",
        "close_probability": 0.25,
        "owner_id": "SR-100",
        "close_date": "2024-07-15",
        "notes": "Needs assessment call scheduled",
    },
}


@tool()
def get_deal_details(deal_id: str):
    """
    Retrieves detailed information about a sales deal.

    Args:
        deal_id: The unique deal identifier (e.g. "D-100").

    Returns:
        Deal details including account name, value, stage, close probability, owner, and notes, or None if not found.
    """
    normalized = str(deal_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
