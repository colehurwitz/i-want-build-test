from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("chicago", "new york", 15.0, "express"): {
        "origin": "Chicago",
        "destination": "New York",
        "weight_kg": 15.0,
        "service_level": "express",
        "rates": [
            {"carrier": "FastFreight", "rate": 45.50, "transit_days": 2, "rating": 4.5},
            {"carrier": "SpeedShip", "rate": 52.00, "transit_days": 2, "rating": 4.2},
            {"carrier": "AirExpress", "rate": 68.00, "transit_days": 1, "rating": 4.8},
        ],
    },
    ("chicago", "los angeles", 25.0, "express"): {
        "origin": "Chicago",
        "destination": "Los Angeles",
        "weight_kg": 25.0,
        "service_level": "express",
        "rates": [
            {"carrier": "FastFreight", "rate": 78.00, "transit_days": 3, "rating": 4.5},
            {"carrier": "SpeedShip", "rate": 85.00, "transit_days": 2, "rating": 4.2},
            {"carrier": "AirExpress", "rate": 110.00, "transit_days": 1, "rating": 4.8},
        ],
    },
    ("new york", "boston", 10.0, "ground"): {
        "origin": "New York",
        "destination": "Boston",
        "weight_kg": 10.0,
        "service_level": "ground",
        "rates": [
            {"carrier": "GroundShip Co", "rate": 18.50, "transit_days": 5, "rating": 4.0},
            {"carrier": "EcoFreight", "rate": 15.00, "transit_days": 7, "rating": 3.8},
            {"carrier": "FastFreight", "rate": 22.00, "transit_days": 4, "rating": 4.5},
        ],
    },
    ("new york", "miami", 8.0, "overnight"): {
        "origin": "New York",
        "destination": "Miami",
        "weight_kg": 8.0,
        "service_level": "overnight",
        "rates": [
            {"carrier": "AirExpress", "rate": 95.00, "transit_days": 1, "rating": 4.8},
            {"carrier": "SpeedShip", "rate": 88.00, "transit_days": 1, "rating": 4.2},
        ],
    },
}


@tool()
def get_carrier_rates(origin: str, destination: str, weight_kg: float, service_level: str):
    """
    Gets shipping rates from available carriers for a given route and service level.

    Args:
        origin: The origin city (e.g. "Chicago").
        destination: The destination city (e.g. "New York").
        weight_kg: The total package weight in kilograms.
        service_level: The desired service level ("ground", "express", or "overnight").

    Returns:
        Available carrier rates with transit times and ratings, or None if no rates found.
    """
    key = (
        str(origin).lower().strip(),
        str(destination).lower().strip(),
        float(weight_kg),
        str(service_level).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
