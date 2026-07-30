from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("entity-a", "reg-100"): {
        "entity": "Entity-A",
        "regulation_id": "REG-100",
        "compliance_score": 45,
        "status": "non_compliant",
        "gaps": [
            {"requirement_id": "REQ-100-A", "status": "fail", "detail": "Processing activity records incomplete — 30% of activities undocumented"},
            {"requirement_id": "REQ-100-B", "status": "fail", "detail": "No breach notification process documented"},
            {"requirement_id": "REQ-100-C", "status": "fail", "detail": "No DPIA conducted in the last 18 months"},
            {"requirement_id": "REQ-100-D", "status": "pass", "detail": "DPO appointed and active"},
            {"requirement_id": "REQ-100-E", "status": "partial", "detail": "DSAR handling averages 45 days — exceeds 30-day requirement"},
        ],
        "assessed_at": "2024-07-29",
    },
    ("entity-b", "reg-200"): {
        "entity": "Entity-B",
        "regulation_id": "REG-200",
        "compliance_score": 55,
        "status": "partially_compliant",
        "gaps": [
            {"requirement_id": "REQ-200-A", "status": "partial", "detail": "AML controls exist but are outdated — last updated 2022"},
            {"requirement_id": "REQ-200-B", "status": "fail", "detail": "Suspicious transaction reports often filed after 48 hours"},
            {"requirement_id": "REQ-200-C", "status": "pass", "detail": "Quarterly risk assessments on schedule"},
            {"requirement_id": "REQ-200-D", "status": "partial", "detail": "CDD records incomplete for 15% of customers"},
        ],
        "assessed_at": "2024-07-29",
    },
    ("entity-c", "reg-300"): {
        "entity": "Entity-C",
        "regulation_id": "REG-300",
        "compliance_score": 85,
        "status": "compliant",
        "gaps": [
            {"requirement_id": "REQ-300-A", "status": "pass", "detail": "All PHI encrypted at rest (AES-256) and in transit (TLS 1.3)"},
            {"requirement_id": "REQ-300-B", "status": "pass", "detail": "RBAC implemented with quarterly access reviews"},
            {"requirement_id": "REQ-300-C", "status": "partial", "detail": "Audit trails exist but retention period is 6 months — regulation requires 12 months"},
        ],
        "assessed_at": "2024-07-29",
    },
    ("entity-c", "reg-400"): {
        "entity": "Entity-C",
        "regulation_id": "REG-400",
        "compliance_score": 72,
        "status": "partially_compliant",
        "gaps": [
            {"requirement_id": "REQ-400-A", "status": "pass", "detail": "Scope 1 and 2 emissions reported, Scope 3 incomplete"},
            {"requirement_id": "REQ-400-B", "status": "partial", "detail": "Reduction targets set but not publicly published"},
            {"requirement_id": "REQ-400-C", "status": "fail", "detail": "No third-party verification conducted"},
        ],
        "assessed_at": "2024-07-29",
    },
    ("entity-d", "reg-100"): {
        "entity": "Entity-D",
        "regulation_id": "REG-100",
        "compliance_score": 90,
        "status": "compliant",
        "gaps": [
            {"requirement_id": "REQ-100-A", "status": "pass", "detail": "Complete processing activity records maintained"},
            {"requirement_id": "REQ-100-B", "status": "pass", "detail": "Breach notification process tested and documented"},
            {"requirement_id": "REQ-100-C", "status": "pass", "detail": "Annual DPIA completed June 2024"},
            {"requirement_id": "REQ-100-D", "status": "pass", "detail": "DPO appointed and active"},
            {"requirement_id": "REQ-100-E", "status": "pass", "detail": "DSAR handling averages 12 days"},
        ],
        "assessed_at": "2024-07-29",
    },
    ("entity-e", "reg-500"): {
        "entity": "Entity-E",
        "regulation_id": "REG-500",
        "compliance_score": 30,
        "status": "non_compliant",
        "gaps": [
            {"requirement_id": "REQ-500-A", "status": "fail", "detail": "No AI system inventory exists"},
            {"requirement_id": "REQ-500-B", "status": "fail", "detail": "No bias or fairness assessments conducted"},
            {"requirement_id": "REQ-500-C", "status": "fail", "detail": "No transparency reports published"},
            {"requirement_id": "REQ-500-D", "status": "partial", "detail": "Human oversight exists for some systems but not all automated decisions"},
        ],
        "assessed_at": "2024-07-29",
    },
}


@tool()
def assess_compliance_status(entity: str, regulation_id: str):
    """
    Assesses an entity's compliance status against a specific regulation.

    Args:
        entity: The business entity name (e.g. "Entity-A").
        regulation_id: The regulation identifier to assess against (e.g. "REG-100").

    Returns:
        Compliance assessment including score (0-100), status, and list of gaps with requirement-level pass/fail details, or None if not found.
    """
    key = (
        str(entity).lower().strip(),
        str(regulation_id).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
