from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "l-100": {
        "lead_id": "L-100",
        "score": 85,
        "grade": "A",
        "engagement_level": "high",
        "factors": ["large_company", "high_web_activity", "downloaded_whitepaper"],
    },
    "l-200": {
        "lead_id": "L-200",
        "score": 30,
        "grade": "D",
        "engagement_level": "low",
        "factors": ["small_company", "single_page_visit"],
    },
    "l-300": {
        "lead_id": "L-300",
        "score": 60,
        "grade": "B",
        "engagement_level": "medium",
        "factors": ["mid_size_company", "attended_event", "opened_emails"],
    },
    "l-400": {
        "lead_id": "L-400",
        "score": 75,
        "grade": "A",
        "engagement_level": "high",
        "factors": ["tech_industry_fit", "multiple_page_visits", "requested_demo"],
    },
    "l-500": {
        "lead_id": "L-500",
        "score": 55,
        "grade": "C",
        "engagement_level": "medium",
        "factors": ["large_company", "low_email_engagement"],
    },
}


@tool()
def score_lead(lead_id: str, engagement_data: dict):
    """
    Scores a sales lead based on their profile and engagement data.

    Args:
        lead_id: The unique lead identifier (e.g. "L-100").
        engagement_data: A dictionary of engagement metrics (e.g. {"page_visits": 12, "emails_opened": 8}).

    Returns:
        Lead scoring results including numeric score, grade, engagement level, and contributing factors, or None if not found.
    """
    normalized = str(lead_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
