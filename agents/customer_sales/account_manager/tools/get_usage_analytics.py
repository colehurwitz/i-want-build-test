from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("a-100", "q2"): {
        "account_id": "A-100",
        "period": "Q2",
        "active_users": 150,
        "active_users_change_pct": 12.0,
        "api_calls": 450000,
        "api_calls_change_pct": 18.5,
        "storage_used_gb": 120.5,
        "feature_adoption": {"analytics": 0.85, "automation": 0.72, "reporting": 0.90, "integrations": 0.60},
        "usage_trend": "growing",
    },
    ("a-200", "q2"): {
        "account_id": "A-200",
        "period": "Q2",
        "active_users": 80,
        "active_users_change_pct": -28.0,
        "api_calls": 120000,
        "api_calls_change_pct": -35.0,
        "storage_used_gb": 45.2,
        "feature_adoption": {"analytics": 0.40, "automation": 0.25, "reporting": 0.55, "integrations": 0.15},
        "usage_trend": "declining",
    },
    ("a-300", "q2"): {
        "account_id": "A-300",
        "period": "Q2",
        "active_users": 35,
        "active_users_change_pct": -22.0,
        "api_calls": 85000,
        "api_calls_change_pct": -15.0,
        "storage_used_gb": 28.0,
        "feature_adoption": {"analytics": 0.60, "automation": 0.45, "reporting": 0.70, "integrations": 0.30},
        "usage_trend": "declining",
    },
    ("a-400", "q2"): {
        "account_id": "A-400",
        "period": "Q2",
        "active_users": 220,
        "active_users_change_pct": 15.0,
        "api_calls": 680000,
        "api_calls_change_pct": 22.0,
        "storage_used_gb": 200.0,
        "feature_adoption": {"analytics": 0.95, "automation": 0.88, "reporting": 0.92, "integrations": 0.80},
        "usage_trend": "growing",
    },
    ("a-500", "q2"): {
        "account_id": "A-500",
        "period": "Q2",
        "active_users": 95,
        "active_users_change_pct": 8.0,
        "api_calls": 280000,
        "api_calls_change_pct": 10.0,
        "storage_used_gb": 75.0,
        "feature_adoption": {"analytics": 0.75, "automation": 0.65, "reporting": 0.80, "integrations": 0.50},
        "usage_trend": "stable",
    },
    ("a-100", "q3"): {
        "account_id": "A-100",
        "period": "Q3",
        "active_users": 165,
        "active_users_change_pct": 10.0,
        "api_calls": 520000,
        "api_calls_change_pct": 15.5,
        "storage_used_gb": 135.0,
        "feature_adoption": {"analytics": 0.88, "automation": 0.78, "reporting": 0.92, "integrations": 0.65},
        "usage_trend": "growing",
    },
    ("a-500", "q3"): {
        "account_id": "A-500",
        "period": "Q3",
        "active_users": 110,
        "active_users_change_pct": 15.8,
        "api_calls": 320000,
        "api_calls_change_pct": 14.3,
        "storage_used_gb": 88.0,
        "feature_adoption": {"analytics": 0.80, "automation": 0.70, "reporting": 0.85, "integrations": 0.55},
        "usage_trend": "growing",
    },
}


@tool()
def get_usage_analytics(account_id: str, period: str):
    """
    Retrieves usage analytics for an account over a specific period.

    Args:
        account_id: The unique account identifier (e.g. "A-100").
        period: The time period for analytics (e.g. "Q2", "Q3", "last_90_days").

    Returns:
        Usage analytics including active users, API calls, storage, feature adoption, and trend, or None if not found.
    """
    key = (
        str(account_id).lower().strip(),
        str(period).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
