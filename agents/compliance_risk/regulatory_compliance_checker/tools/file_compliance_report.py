from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("entity-a", "reg-100", "non_compliant"): {
        "report_id": "CRP-9001",
        "entity": "Entity-A",
        "regulation_id": "REG-100",
        "status": "non_compliant",
        "filed_at": "2024-07-29T10:00:00Z",
        "acknowledgment": "Report filed successfully. Compliance officer will be notified of critical findings.",
        "next_review_date": "2024-10-29",
    },
    ("entity-b", "reg-200", "non_compliant"): {
        "report_id": "CRP-9002",
        "entity": "Entity-B",
        "regulation_id": "REG-200",
        "status": "non_compliant",
        "filed_at": "2024-07-29T10:05:00Z",
        "acknowledgment": "Report filed. ESCALATION: Repeat offender status — 4 violations for REG-200. Immediate compliance officer notification required.",
        "next_review_date": "2024-08-29",
    },
    ("entity-c", "reg-300", "compliant"): {
        "report_id": "CRP-9003",
        "entity": "Entity-C",
        "regulation_id": "REG-300",
        "status": "compliant",
        "filed_at": "2024-07-29T10:10:00Z",
        "acknowledgment": "Report filed. Entity is compliant with minor recommendations for improvement.",
        "next_review_date": "2025-01-29",
    },
    ("entity-c", "reg-400", "partially_compliant"): {
        "report_id": "CRP-9004",
        "entity": "Entity-C",
        "regulation_id": "REG-400",
        "status": "partially_compliant",
        "filed_at": "2024-07-29T10:12:00Z",
        "acknowledgment": "Report filed. Remediation required for third-party verification and Scope 3 reporting.",
        "next_review_date": "2024-10-29",
    },
    ("entity-d", "reg-100", "compliant"): {
        "report_id": "CRP-9005",
        "entity": "Entity-D",
        "regulation_id": "REG-100",
        "status": "compliant",
        "filed_at": "2024-07-29T10:15:00Z",
        "acknowledgment": "Report filed. Entity is fully compliant.",
        "next_review_date": "2025-07-29",
    },
    ("entity-e", "reg-500", "non_compliant"): {
        "report_id": "CRP-9006",
        "entity": "Entity-E",
        "regulation_id": "REG-500",
        "status": "non_compliant",
        "filed_at": "2024-07-29T10:20:00Z",
        "acknowledgment": "Report filed. CRITICAL: Compliance score 30% — immediate action required before regulation effective date.",
        "next_review_date": "2024-08-15",
    },
    ("entity-b", "reg-200", "partially_compliant"): {
        "report_id": "CRP-9007",
        "entity": "Entity-B",
        "regulation_id": "REG-200",
        "status": "partially_compliant",
        "filed_at": "2024-07-29T10:25:00Z",
        "acknowledgment": "Report filed. ESCALATION: Repeat offender with 4 violations.",
        "next_review_date": "2024-08-29",
    },
}


@tool()
def file_compliance_report(entity: str, regulation_id: str, status: str, findings: str, remediation_plan: str):
    """
    Files a compliance report for an entity against a regulation.

    Args:
        entity: The business entity name (e.g. "Entity-A").
        regulation_id: The regulation identifier (e.g. "REG-100").
        status: The compliance status — one of "compliant", "partially_compliant", or "non_compliant".
        findings: Detailed findings including gaps, requirement IDs, and violation references.
        remediation_plan: Planned remediation actions with timelines and responsible parties.

    Returns:
        Report filing confirmation including report_id, acknowledgment, and next review date, or None if filing failed.
    """
    key = (
        str(entity).lower().strip(),
        str(regulation_id).lower().strip(),
        str(status).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
