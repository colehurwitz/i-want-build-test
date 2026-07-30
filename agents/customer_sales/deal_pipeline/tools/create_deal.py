from ibm_watsonx_orchestrate.agent_builder.tools import tool

_D600 = {
    "deal_id": "D-600",
    "status": "created",
    "account_id": "A-200",
    "title": "New Enterprise Deal",
    "value": 50000.00,
    "stage": "prospecting",
    "owner_id": "SR-100",
    "created_at": "2024-03-15T15:00:00Z",
}
_D700 = {
    "deal_id": "D-700",
    "status": "created",
    "account_id": "A-300",
    "title": "A-300 Platform Expansion",
    "value": 100000.00,
    "stage": "prospecting",
    "owner_id": "SR-200",
    "created_at": "2024-03-15T16:00:00Z",
}

STUB_RESPONSES = {
    ("a-200", "new enterprise deal", 50000.0, "prospecting", "sr-100"): _D600,
    ("a-200", "enterprise deal", 50000.0, "prospecting", "sr-100"): _D600,
    ("a-300", "a-300 platform expansion", 100000.0, "prospecting", "sr-200"): _D700,
    ("a-300", "platform expansion", 100000.0, "prospecting", "sr-200"): _D700,
    ("a-300", "new strategic partnership", 100000.0, "prospecting", "sr-200"): _D700,
    ("a-300", "strategic partnership", 100000.0, "prospecting", "sr-200"): _D700,
    ("a-300", "new deal", 100000.0, "prospecting", "sr-200"): _D700,
    ("a-300", "expansion deal", 100000.0, "prospecting", "sr-200"): _D700,
}


@tool()
def create_deal(account_id: str, title: str, value: float, stage: str, owner_id: str):
    """
    Creates a new deal in the sales pipeline.

    Args:
        account_id: The account identifier (e.g. "A-200").
        title: The deal title.
        value: The deal value in USD.
        stage: The initial deal stage ("prospecting", "qualification", "proposal", "negotiation").
        owner_id: The sales rep who owns the deal (e.g. "SR-100").

    Returns:
        Created deal details including deal_id and status, or None if creation failed.
    """
    key = (
        str(account_id).lower().strip(),
        str(title).lower().strip(),
        float(value),
        str(stage).lower().strip(),
        str(owner_id).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
