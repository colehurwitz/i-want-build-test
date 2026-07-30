from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("d-100", "proposal", 0.5): {
        "deal_id": "D-100",
        "status": "updated",
        "previous_stage": "qualification",
        "new_stage": "proposal",
        "close_probability": 0.50,
        "updated_at": "2024-03-15T10:00:00Z",
    },
    ("d-200", "closed_won", 1.0): {
        "deal_id": "D-200",
        "status": "updated",
        "previous_stage": "negotiation",
        "new_stage": "closed_won",
        "close_probability": 1.00,
        "updated_at": "2024-03-15T11:00:00Z",
    },
    ("d-300", "qualification", 0.25): {
        "deal_id": "D-300",
        "status": "updated",
        "previous_stage": "prospecting",
        "new_stage": "qualification",
        "close_probability": 0.25,
        "updated_at": "2024-03-15T12:00:00Z",
    },
    ("d-400", "negotiation", 0.75): {
        "deal_id": "D-400",
        "status": "updated",
        "previous_stage": "proposal",
        "new_stage": "negotiation",
        "close_probability": 0.75,
        "updated_at": "2024-03-15T13:00:00Z",
    },
    ("d-200", "closed_lost", 0.0): {
        "deal_id": "D-200",
        "status": "updated",
        "previous_stage": "negotiation",
        "new_stage": "closed_lost",
        "close_probability": 0.00,
        "updated_at": "2024-03-15T14:00:00Z",
    },
}


@tool()
def update_deal_stage(deal_id: str, new_stage: str, close_probability: float, notes: str):
    """
    Updates the stage and close probability of a deal.

    Args:
        deal_id: The unique deal identifier (e.g. "D-100").
        new_stage: The new deal stage ("prospecting", "qualification", "proposal", "negotiation", "closed_won", "closed_lost").
        close_probability: The updated probability of closing (0.0 to 1.0).
        notes: Notes explaining the stage change.

    Returns:
        Update confirmation including previous and new stage, or None if update failed.
    """
    key = (
        str(deal_id).lower().strip(),
        str(new_stage).lower().strip(),
        float(close_probability),
    )
    return STUB_RESPONSES.get(key)
