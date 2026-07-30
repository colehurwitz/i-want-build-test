from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "trk-200-exp": {
        "tracking_number": "TRK-200-EXP",
        "shipment_id": "SHP-200",
        "status": "in_transit",
        "carrier": "FastFreight",
        "origin": "Dallas",
        "destination": "Seattle",
        "current_location": "Denver, CO",
        "estimated_delivery": "2026-08-01",
        "events": [
            {"timestamp": "2026-07-28T08:00:00Z", "location": "Dallas, TX", "event": "Picked up"},
            {"timestamp": "2026-07-28T18:00:00Z", "location": "Amarillo, TX", "event": "In transit"},
            {"timestamp": "2026-07-29T10:00:00Z", "location": "Denver, CO", "event": "Arrived at hub"},
        ],
    },
    "trk-201-gnd": {
        "tracking_number": "TRK-201-GND",
        "shipment_id": "SHP-201",
        "status": "delivered",
        "carrier": "GroundShip Co",
        "origin": "Atlanta",
        "destination": "Charlotte",
        "current_location": "Charlotte, NC",
        "estimated_delivery": "2026-07-27",
        "delivered_at": "2026-07-27T14:30:00Z",
        "events": [
            {"timestamp": "2026-07-24T09:00:00Z", "location": "Atlanta, GA", "event": "Picked up"},
            {"timestamp": "2026-07-27T14:30:00Z", "location": "Charlotte, NC", "event": "Delivered"},
        ],
    },
    "trk-202-exp": {
        "tracking_number": "TRK-202-EXP",
        "shipment_id": "SHP-202",
        "status": "delayed",
        "carrier": "SpeedShip",
        "origin": "San Francisco",
        "destination": "Portland",
        "current_location": "Sacramento, CA",
        "estimated_delivery": "2026-08-03",
        "original_estimate": "2026-07-30",
        "delay_reason": "Weather conditions",
        "events": [
            {"timestamp": "2026-07-27T07:00:00Z", "location": "San Francisco, CA", "event": "Picked up"},
            {"timestamp": "2026-07-28T12:00:00Z", "location": "Sacramento, CA", "event": "Delayed - weather"},
        ],
    },
    "trk-203-pnd": {
        "tracking_number": "TRK-203-PND",
        "shipment_id": "SHP-203",
        "status": "pending",
        "carrier": "FastFreight",
        "origin": "Chicago",
        "destination": "Detroit",
        "current_location": "Chicago, IL",
        "estimated_delivery": "2026-08-02",
        "events": [
            {"timestamp": "2026-07-29T06:00:00Z", "location": "Chicago, IL", "event": "Label created"},
        ],
    },
}


@tool()
def track_shipment(tracking_number: str):
    """
    Tracks a shipment using its tracking number.

    Args:
        tracking_number: The shipment tracking number (e.g. "TRK-200-EXP").

    Returns:
        Tracking details including status, current location, and event history, or None if not found.
    """
    normalized = str(tracking_number).lower().strip()
    return STUB_RESPONSES.get(normalized)
