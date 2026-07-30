from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("chicago", "new york", "express"): {
        "origin": "Chicago",
        "destination": "New York",
        "service_level": "express",
        "estimated_days": 2,
        "estimated_delivery_date": "2026-08-02",
        "confidence": "high",
    },
    ("chicago", "los angeles", "express"): {
        "origin": "Chicago",
        "destination": "Los Angeles",
        "service_level": "express",
        "estimated_days": 3,
        "estimated_delivery_date": "2026-08-03",
        "confidence": "high",
    },
    ("new york", "boston", "ground"): {
        "origin": "New York",
        "destination": "Boston",
        "service_level": "ground",
        "estimated_days": 5,
        "estimated_delivery_date": "2026-08-05",
        "confidence": "medium",
    },
    ("new york", "miami", "overnight"): {
        "origin": "New York",
        "destination": "Miami",
        "service_level": "overnight",
        "estimated_days": 1,
        "estimated_delivery_date": "2026-07-31",
        "confidence": "high",
    },
}


@tool()
def get_delivery_estimate(origin: str, destination: str, service_level: str):
    """
    Gets an estimated delivery date for a shipment route and service level.

    Args:
        origin: The origin city (e.g. "Chicago").
        destination: The destination city (e.g. "New York").
        service_level: The service level ("ground", "express", or "overnight").

    Returns:
        Delivery estimate with estimated days, date, and confidence level, or None if route not available.
    """
    key = (
        str(origin).lower().strip(),
        str(destination).lower().strip(),
        str(service_level).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
