from ibm_watsonx_orchestrate.agent_builder.tools import tool
from typing import List

STUB_RESPONSES = {
    ("q-7001", "q-7002", "q-7003"): {
        "comparison_table": [
            {"vendor": "KeyTech Pro", "quote_id": "Q-7001", "unit_price": 145.00, "total": 7250.00, "delivery_days": 16, "rating": 4.5},
            {"vendor": "ErgoSupply Co", "quote_id": "Q-7002", "unit_price": 135.00, "total": 6750.00, "delivery_days": 13, "rating": 4.2},
            {"vendor": "Office Gear Direct", "quote_id": "Q-7003", "unit_price": 155.00, "total": 7750.00, "delivery_days": 23, "rating": 3.8},
        ],
        "recommended_vendor": "ErgoSupply Co",
        "recommended_quote_id": "Q-7002",
        "recommendation_reason": "Lowest price ($6,750) with fastest delivery (13 days) and good rating (4.2)",
        "savings_vs_average": 500.00,
    },
    ("q-7006", "q-7007"): {
        "comparison_table": [
            {"vendor": "DisplayTech", "quote_id": "Q-7006", "unit_price": 420.00, "total": 42000.00, "delivery_days": 16, "rating": 4.4},
            {"vendor": "ScreenPro Global", "quote_id": "Q-7007", "unit_price": 380.00, "total": 38000.00, "delivery_days": 25, "rating": 4.1},
        ],
        "recommended_vendor": "ScreenPro Global",
        "recommended_quote_id": "Q-7007",
        "recommendation_reason": "Lower price ($38,000 vs $42,000) despite longer delivery. $4,000 savings.",
        "savings_vs_average": 2000.00,
    },
    ("q-7008", "q-7009"): {
        "comparison_table": [
            {"vendor": "AudioPro", "quote_id": "Q-7008", "unit_price": 89.00, "total": 1780.00, "delivery_days": 10, "rating": 4.6},
            {"vendor": "SoundGear Inc", "quote_id": "Q-7009", "unit_price": 75.00, "total": 1500.00, "delivery_days": 15, "rating": 4.0},
        ],
        "recommended_vendor": "SoundGear Inc",
        "recommended_quote_id": "Q-7009",
        "recommendation_reason": "Lowest price ($1,500) with acceptable delivery timeline and good rating.",
        "savings_vs_average": 140.00,
    },
}


@tool()
def compare_quotes(quote_ids: List[str]):
    """
    Compares multiple vendor quotes side-by-side and provides a recommendation.

    Args:
        quote_ids: List of quote IDs to compare (e.g. ["Q-7001", "Q-7002", "Q-7003"]).

    Returns:
        Comparison including a table of all quotes, the recommended vendor, recommendation reason, and potential savings, or None if comparison failed.
    """
    key = tuple(sorted(str(q).lower().strip() for q in quote_ids))
    return STUB_RESPONSES.get(key)
