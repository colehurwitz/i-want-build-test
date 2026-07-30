from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "entity-a": {
        "entity": "Entity-A",
        "total_violations": 2,
        "violations": [
            {
                "violation_id": "VIO-101",
                "regulation_id": "REG-100",
                "date": "2023-06-15",
                "description": "Failed to complete DPIA within required timeframe",
                "severity": "medium",
                "status": "resolved",
                "fine_amount": "$50,000",
            },
            {
                "violation_id": "VIO-102",
                "regulation_id": "REG-100",
                "date": "2024-01-20",
                "description": "DSAR response exceeded 30-day deadline for 12 subjects",
                "severity": "high",
                "status": "unresolved",
                "fine_amount": "$150,000",
            },
        ],
        "repeat_offender": False,
    },
    "entity-b": {
        "entity": "Entity-B",
        "total_violations": 4,
        "violations": [
            {
                "violation_id": "VIO-201",
                "regulation_id": "REG-200",
                "date": "2022-09-01",
                "description": "Late filing of suspicious transaction report",
                "severity": "high",
                "status": "resolved",
                "fine_amount": "$200,000",
            },
            {
                "violation_id": "VIO-202",
                "regulation_id": "REG-200",
                "date": "2023-03-15",
                "description": "Incomplete customer due diligence records",
                "severity": "medium",
                "status": "resolved",
                "fine_amount": "$100,000",
            },
            {
                "violation_id": "VIO-203",
                "regulation_id": "REG-200",
                "date": "2023-11-20",
                "description": "Late filing of suspicious transaction report",
                "severity": "high",
                "status": "resolved",
                "fine_amount": "$300,000",
            },
            {
                "violation_id": "VIO-204",
                "regulation_id": "REG-200",
                "date": "2024-05-10",
                "description": "Late filing of suspicious transaction report — third occurrence",
                "severity": "critical",
                "status": "unresolved",
                "fine_amount": "$500,000",
            },
        ],
        "repeat_offender": True,
    },
    "entity-c": {
        "entity": "Entity-C",
        "total_violations": 0,
        "violations": [],
        "repeat_offender": False,
    },
    "entity-d": {
        "entity": "Entity-D",
        "total_violations": 1,
        "violations": [
            {
                "violation_id": "VIO-401",
                "regulation_id": "REG-100",
                "date": "2022-12-01",
                "description": "Minor documentation gap in processing activity records",
                "severity": "low",
                "status": "resolved",
                "fine_amount": "$10,000",
            },
        ],
        "repeat_offender": False,
    },
    "entity-e": {
        "entity": "Entity-E",
        "total_violations": 0,
        "violations": [],
        "repeat_offender": False,
    },
}


@tool()
def get_violation_history(entity: str):
    """
    Retrieves the violation history for a business entity across all regulations.

    Args:
        entity: The business entity name (e.g. "Entity-A").

    Returns:
        Violation history including total count, individual violations with dates/severity/status/fines, and whether entity is a repeat offender, or None if not found.
    """
    normalized = str(entity).lower().strip()
    return STUB_RESPONSES.get(normalized)
