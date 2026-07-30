from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "l-100": {
        "lead_id": "L-100",
        "name": "Alice Johnson",
        "company": "BigCorp Industries",
        "industry": "manufacturing",
        "company_size": 5000,
        "source": "website",
        "status": "new",
        "email": "alice@bigcorp.com",
        "engagement": {"page_visits": 12, "emails_opened": 8, "content_downloaded": 3},
    },
    "l-200": {
        "lead_id": "L-200",
        "name": "Bob Martinez",
        "company": "TinyStart LLC",
        "industry": "technology",
        "company_size": 15,
        "source": "referral",
        "status": "contacted",
        "email": "bob@tinystart.io",
        "engagement": {"page_visits": 2, "emails_opened": 1, "content_downloaded": 0},
    },
    "l-300": {
        "lead_id": "L-300",
        "name": "Carol Davis",
        "company": "MidRange Solutions",
        "industry": "consulting",
        "company_size": 250,
        "source": "trade_show",
        "status": "new",
        "email": "carol@midrange.com",
        "engagement": {"page_visits": 6, "emails_opened": 4, "content_downloaded": 1},
    },
    "l-400": {
        "lead_id": "L-400",
        "name": "Dan Kim",
        "company": "TechForward Inc",
        "industry": "technology",
        "company_size": 800,
        "source": "webinar",
        "status": "new",
        "email": "dan@techforward.com",
        "engagement": {"page_visits": 15, "emails_opened": 10, "content_downloaded": 4},
    },
    "l-500": {
        "lead_id": "L-500",
        "name": "Eva Chen",
        "company": "RetailMax",
        "industry": "retail",
        "company_size": 1200,
        "source": "cold_outreach",
        "status": "new",
        "email": "eva@retailmax.com",
        "engagement": {"page_visits": 5, "emails_opened": 3, "content_downloaded": 1},
    },
}


@tool()
def get_lead_info(lead_id: str):
    """
    Retrieves detailed information about a sales lead.

    Args:
        lead_id: The unique lead identifier (e.g. "L-100").

    Returns:
        Lead details including name, company, industry, company size, source, status, and engagement data, or None if not found.
    """
    normalized = str(lead_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
