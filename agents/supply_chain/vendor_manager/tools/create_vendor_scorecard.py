from ibm_watsonx_orchestrate.agent_builder.tools import tool
from typing import List

STUB_RESPONSES = {
    ("v-100", "q2-2026"): {
        "vendor_id": "V-100",
        "period": "Q2-2026",
        "scorecard_id": "SC-100-Q2",
        "scores": {
            "delivery": 9.5,
            "quality": 9.3,
            "pricing": 8.8,
            "responsiveness": 9.0,
            "innovation": 9.2,
        },
        "overall_score": 9.2,
        "rating": "Excellent",
        "recommendation": "Maintain preferred vendor status. Consider expanding partnership to new categories.",
        "previous_score": 9.0,
        "trend": "improving",
    },
    ("v-200", "q2-2026"): {
        "vendor_id": "V-200",
        "period": "Q2-2026",
        "scorecard_id": "SC-200-Q2",
        "scores": {
            "delivery": 5.5,
            "quality": 5.0,
            "pricing": 6.5,
            "responsiveness": 4.8,
            "innovation": 3.0,
        },
        "overall_score": 5.0,
        "rating": "Adequate",
        "recommendation": "Issue performance improvement plan. Increase monitoring frequency. Review in 30 days.",
        "previous_score": 7.2,
        "trend": "declining",
    },
    ("v-300", "q2-2026"): {
        "vendor_id": "V-300",
        "period": "Q2-2026",
        "scorecard_id": "SC-300-Q2",
        "scores": {
            "delivery": 7.8,
            "quality": 7.5,
            "pricing": 8.0,
            "responsiveness": 7.2,
            "innovation": 5.5,
        },
        "overall_score": 7.2,
        "rating": "Good",
        "recommendation": "Maintain relationship. Encourage innovation and sustainability initiatives.",
        "previous_score": 7.0,
        "trend": "stable",
    },
    ("v-400", "q2-2026"): {
        "vendor_id": "V-400",
        "period": "Q2-2026",
        "scorecard_id": "SC-400-Q2",
        "scores": {
            "delivery": 8.2,
            "quality": 8.0,
            "pricing": 8.5,
            "responsiveness": 7.8,
            "innovation": 8.0,
        },
        "overall_score": 8.1,
        "rating": "Good",
        "recommendation": "Strong performer. Consider upgrading to preferred tier at next contract renewal.",
        "previous_score": 7.8,
        "trend": "improving",
    },
    ("v-500", "q2-2026"): {
        "vendor_id": "V-500",
        "period": "Q2-2026",
        "scorecard_id": "SC-500-Q2",
        "scores": {
            "delivery": 2.5,
            "quality": 2.0,
            "pricing": 3.5,
            "responsiveness": 2.0,
            "innovation": 1.0,
        },
        "overall_score": 2.2,
        "rating": "Unacceptable",
        "recommendation": "Initiate vendor transition plan. Stop placing new orders. Begin offboarding process.",
        "previous_score": 3.8,
        "trend": "declining",
    },
}


@tool()
def create_vendor_scorecard(vendor_id: str, period: str, categories: List[str]):
    """
    Creates a performance scorecard for a vendor based on specified evaluation categories.

    Args:
        vendor_id: The vendor identifier (e.g. "V-100").
        period: The evaluation period (e.g. "Q2-2026").
        categories: List of categories to evaluate (e.g. ["delivery", "quality", "pricing", "responsiveness", "innovation"]).

    Returns:
        Scorecard with scores per category, overall rating, recommendation, and trend, or None if creation failed.
    """
    key = (
        str(vendor_id).lower().strip(),
        str(period).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
