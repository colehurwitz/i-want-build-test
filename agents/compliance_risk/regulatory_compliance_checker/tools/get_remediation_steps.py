from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "documentation": {
        "violation_type": "documentation",
        "steps": [
            {"step": 1, "action": "Audit all current documentation for completeness", "timeline": "2 weeks", "responsible": "Compliance Team"},
            {"step": 2, "action": "Create templates for missing documentation categories", "timeline": "1 week", "responsible": "Compliance Team"},
            {"step": 3, "action": "Populate all required records with current data", "timeline": "4 weeks", "responsible": "Department Heads"},
            {"step": 4, "action": "Implement automated documentation tracking system", "timeline": "8 weeks", "responsible": "IT + Compliance"},
        ],
        "estimated_total_timeline": "15 weeks",
        "priority": "high",
    },
    "incident_response": {
        "violation_type": "incident_response",
        "steps": [
            {"step": 1, "action": "Draft incident response and breach notification procedures", "timeline": "2 weeks", "responsible": "Security Team"},
            {"step": 2, "action": "Establish notification templates and communication channels", "timeline": "1 week", "responsible": "Legal + Communications"},
            {"step": 3, "action": "Conduct tabletop exercise to test notification process", "timeline": "2 weeks", "responsible": "Security Team + Legal"},
            {"step": 4, "action": "Document lessons learned and refine procedures", "timeline": "1 week", "responsible": "Compliance Team"},
        ],
        "estimated_total_timeline": "6 weeks",
        "priority": "critical",
    },
    "assessment": {
        "violation_type": "assessment",
        "steps": [
            {"step": 1, "action": "Schedule and scope the required assessment (DPIA/risk/bias)", "timeline": "1 week", "responsible": "Compliance Team"},
            {"step": 2, "action": "Conduct the assessment with appropriate stakeholders", "timeline": "4 weeks", "responsible": "Assessment Team"},
            {"step": 3, "action": "Document findings and create remediation roadmap", "timeline": "2 weeks", "responsible": "Compliance Team"},
            {"step": 4, "action": "Implement assessment recommendations", "timeline": "8 weeks", "responsible": "Engineering + Operations"},
        ],
        "estimated_total_timeline": "15 weeks",
        "priority": "high",
    },
    "reporting": {
        "violation_type": "reporting",
        "steps": [
            {"step": 1, "action": "Identify all reporting obligations and deadlines", "timeline": "1 week", "responsible": "Compliance Team"},
            {"step": 2, "action": "Implement automated reporting pipelines", "timeline": "4 weeks", "responsible": "IT + Compliance"},
            {"step": 3, "action": "Establish review and approval workflow for reports", "timeline": "2 weeks", "responsible": "Compliance Team"},
        ],
        "estimated_total_timeline": "7 weeks",
        "priority": "high",
    },
    "financial_controls": {
        "violation_type": "financial_controls",
        "steps": [
            {"step": 1, "action": "Review and update all AML/KYC procedures", "timeline": "3 weeks", "responsible": "Compliance Team"},
            {"step": 2, "action": "Implement real-time transaction monitoring", "timeline": "6 weeks", "responsible": "IT + Finance"},
            {"step": 3, "action": "Train all financial operations staff on updated procedures", "timeline": "2 weeks", "responsible": "Training Team"},
            {"step": 4, "action": "Conduct external audit of updated controls", "timeline": "4 weeks", "responsible": "External Auditor"},
        ],
        "estimated_total_timeline": "15 weeks",
        "priority": "critical",
    },
    "governance": {
        "violation_type": "governance",
        "steps": [
            {"step": 1, "action": "Establish governance committee with clear charter", "timeline": "2 weeks", "responsible": "Executive Team"},
            {"step": 2, "action": "Define oversight policies and procedures", "timeline": "3 weeks", "responsible": "Compliance Team"},
            {"step": 3, "action": "Implement monitoring and reporting dashboards", "timeline": "4 weeks", "responsible": "IT + Compliance"},
        ],
        "estimated_total_timeline": "9 weeks",
        "priority": "high",
    },
}


@tool()
def get_remediation_steps(violation_type: str):
    """
    Retrieves recommended remediation steps for a specific type of compliance violation.

    Args:
        violation_type: The category of violation — one of "documentation", "incident_response", "assessment", "reporting", "financial_controls", "governance", "security", "access_control", "monitoring", or "verification".

    Returns:
        Remediation plan including ordered steps with actions, timelines, responsible parties, and overall estimated timeline, or None if not found.
    """
    normalized = str(violation_type).lower().strip()
    return STUB_RESPONSES.get(normalized)
