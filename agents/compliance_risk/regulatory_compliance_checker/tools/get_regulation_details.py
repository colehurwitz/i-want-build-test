from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "reg-100": {
        "regulation_id": "REG-100",
        "name": "Data Protection and Privacy Act",
        "jurisdiction": "EU",
        "effective_date": "2020-01-01",
        "requirements": [
            {"id": "REQ-100-A", "description": "Maintain records of all processing activities", "category": "documentation"},
            {"id": "REQ-100-B", "description": "Implement data breach notification within 72 hours", "category": "incident_response"},
            {"id": "REQ-100-C", "description": "Conduct annual data protection impact assessments", "category": "assessment"},
            {"id": "REQ-100-D", "description": "Appoint a Data Protection Officer", "category": "governance"},
            {"id": "REQ-100-E", "description": "Ensure data subject access request handling within 30 days", "category": "rights_management"},
        ],
        "penalty_range": "Up to 4% of annual global turnover or EUR 20 million",
        "last_updated": "2024-01-15",
    },
    "reg-200": {
        "regulation_id": "REG-200",
        "name": "Financial Services Compliance Framework",
        "jurisdiction": "US",
        "effective_date": "2019-06-01",
        "requirements": [
            {"id": "REQ-200-A", "description": "Maintain anti-money laundering (AML) controls", "category": "financial_controls"},
            {"id": "REQ-200-B", "description": "Report suspicious transactions within 24 hours", "category": "reporting"},
            {"id": "REQ-200-C", "description": "Conduct quarterly risk assessments", "category": "assessment"},
            {"id": "REQ-200-D", "description": "Maintain customer due diligence records", "category": "documentation"},
        ],
        "penalty_range": "Up to $10 million per violation plus criminal liability",
        "last_updated": "2024-03-01",
    },
    "reg-300": {
        "regulation_id": "REG-300",
        "name": "Healthcare Information Security Standard",
        "jurisdiction": "US",
        "effective_date": "2021-03-15",
        "requirements": [
            {"id": "REQ-300-A", "description": "Encrypt all PHI at rest and in transit", "category": "security"},
            {"id": "REQ-300-B", "description": "Implement role-based access controls for health records", "category": "access_control"},
            {"id": "REQ-300-C", "description": "Maintain audit trails for all PHI access", "category": "monitoring"},
        ],
        "penalty_range": "Up to $1.5 million per violation category per year",
        "last_updated": "2023-11-01",
    },
    "reg-400": {
        "regulation_id": "REG-400",
        "name": "Environmental Reporting Standards",
        "jurisdiction": "Global",
        "effective_date": "2023-01-01",
        "requirements": [
            {"id": "REQ-400-A", "description": "Report annual carbon emissions (Scope 1, 2, 3)", "category": "reporting"},
            {"id": "REQ-400-B", "description": "Set and publish emission reduction targets", "category": "governance"},
            {"id": "REQ-400-C", "description": "Third-party verification of emissions data", "category": "verification"},
        ],
        "penalty_range": "Regulatory fines vary by jurisdiction plus reputational risk",
        "last_updated": "2024-06-01",
    },
    "reg-500": {
        "regulation_id": "REG-500",
        "name": "AI Governance and Transparency Act",
        "jurisdiction": "EU",
        "effective_date": "2024-08-01",
        "requirements": [
            {"id": "REQ-500-A", "description": "Document all AI systems and their intended purposes", "category": "documentation"},
            {"id": "REQ-500-B", "description": "Conduct bias and fairness assessments for high-risk AI", "category": "assessment"},
            {"id": "REQ-500-C", "description": "Provide transparency reports for public-facing AI systems", "category": "reporting"},
            {"id": "REQ-500-D", "description": "Implement human oversight mechanisms for automated decisions", "category": "governance"},
        ],
        "penalty_range": "Up to 6% of annual global turnover or EUR 30 million",
        "last_updated": "2024-07-01",
    },
}


@tool()
def get_regulation_details(regulation_id: str):
    """
    Retrieves the details and requirements of a specific regulation.

    Args:
        regulation_id: The regulation identifier (e.g. "REG-100").

    Returns:
        Regulation details including name, jurisdiction, requirements list, penalty range, and effective date, or None if not found.
    """
    normalized = str(regulation_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
