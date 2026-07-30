from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("v-100", "q2-2026"): {
        "vendor_id": "V-100",
        "period": "Q2-2026",
        "delivery": {"on_time_rate": 0.97, "order_accuracy": 0.99, "avg_lead_days": 12},
        "quality": {"defect_rate": 0.008, "return_rate": 0.005, "spec_compliance": 0.98},
        "pricing": {"competitiveness": "above_average", "invoice_accuracy": 0.995, "discount_adherence": True},
        "responsiveness": {"avg_response_hrs": 2.5, "resolution_days": 1.2, "proactive_updates": True},
        "innovation": {"suggestions": 3, "process_improvements": 1, "sustainability": True},
        "overall_score": 9.2,
    },
    ("v-200", "q2-2026"): {
        "vendor_id": "V-200",
        "period": "Q2-2026",
        "delivery": {"on_time_rate": 0.88, "order_accuracy": 0.94, "avg_lead_days": 18},
        "quality": {"defect_rate": 0.035, "return_rate": 0.02, "spec_compliance": 0.91},
        "pricing": {"competitiveness": "average", "invoice_accuracy": 0.97, "discount_adherence": True},
        "responsiveness": {"avg_response_hrs": 6.0, "resolution_days": 3.5, "proactive_updates": False},
        "innovation": {"suggestions": 0, "process_improvements": 0, "sustainability": False},
        "overall_score": 5.8,
    },
    ("v-300", "q2-2026"): {
        "vendor_id": "V-300",
        "period": "Q2-2026",
        "delivery": {"on_time_rate": 0.92, "order_accuracy": 0.96, "avg_lead_days": 15},
        "quality": {"defect_rate": 0.018, "return_rate": 0.01, "spec_compliance": 0.95},
        "pricing": {"competitiveness": "competitive", "invoice_accuracy": 0.99, "discount_adherence": True},
        "responsiveness": {"avg_response_hrs": 3.5, "resolution_days": 2.0, "proactive_updates": True},
        "innovation": {"suggestions": 1, "process_improvements": 0, "sustainability": False},
        "overall_score": 7.5,
    },
    ("v-400", "q2-2026"): {
        "vendor_id": "V-400",
        "period": "Q2-2026",
        "delivery": {"on_time_rate": 0.93, "order_accuracy": 0.97, "avg_lead_days": 14},
        "quality": {"defect_rate": 0.015, "return_rate": 0.008, "spec_compliance": 0.96},
        "pricing": {"competitiveness": "above_average", "invoice_accuracy": 0.98, "discount_adherence": True},
        "responsiveness": {"avg_response_hrs": 3.0, "resolution_days": 1.8, "proactive_updates": True},
        "innovation": {"suggestions": 2, "process_improvements": 1, "sustainability": True},
        "overall_score": 8.1,
    },
    ("v-500", "q2-2026"): {
        "vendor_id": "V-500",
        "period": "Q2-2026",
        "delivery": {"on_time_rate": 0.72, "order_accuracy": 0.85, "avg_lead_days": 25},
        "quality": {"defect_rate": 0.065, "return_rate": 0.045, "spec_compliance": 0.80},
        "pricing": {"competitiveness": "below_average", "invoice_accuracy": 0.88, "discount_adherence": False},
        "responsiveness": {"avg_response_hrs": 12.0, "resolution_days": 7.0, "proactive_updates": False},
        "innovation": {"suggestions": 0, "process_improvements": 0, "sustainability": False},
        "overall_score": 2.8,
    },
}


@tool()
def get_vendor_performance(vendor_id: str, period: str):
    """
    Retrieves performance metrics for a vendor during a specific period.

    Args:
        vendor_id: The vendor identifier (e.g. "V-100").
        period: The evaluation period (e.g. "Q2-2026").

    Returns:
        Performance data across delivery, quality, pricing, responsiveness, and innovation, or None if not found.
    """
    key = (
        str(vendor_id).lower().strip(),
        str(period).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
