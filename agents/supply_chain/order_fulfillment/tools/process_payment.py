from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("ord-100", "credit_card"): {
        "status": "success",
        "order_id": "ORD-100",
        "payment_id": "PAY-100",
        "amount": 3750.00,
        "method": "credit_card",
        "transaction_ref": "TXN-CC-100",
    },
    ("ord-200", "purchase_order"): {
        "status": "failed",
        "order_id": "ORD-200",
        "error": "Purchase order PO-200 not found in system",
        "method": "purchase_order",
    },
    ("ord-300", "credit_card"): {
        "status": "success",
        "order_id": "ORD-300",
        "payment_id": "PAY-300",
        "amount": 900.00,
        "method": "credit_card",
        "transaction_ref": "TXN-CC-300",
    },
    ("ord-400", "wire_transfer"): {
        "status": "success",
        "order_id": "ORD-400",
        "payment_id": "PAY-400",
        "amount": 1250.00,
        "method": "wire_transfer",
        "transaction_ref": "TXN-WT-400",
    },
    ("ord-600", "credit_card"): {
        "status": "success",
        "order_id": "ORD-600",
        "payment_id": "PAY-600",
        "amount": 300.00,
        "method": "credit_card",
        "transaction_ref": "TXN-CC-600",
    },
}


@tool()
def process_payment(order_id: str, payment_method: str):
    """
    Processes payment for an order using the specified payment method.

    Args:
        order_id: The order identifier (e.g. "ORD-100").
        payment_method: The payment method ("credit_card", "wire_transfer", "purchase_order", "net_30").

    Returns:
        Payment result with transaction reference, or error details if payment failed, or None if order not found.
    """
    key = (
        str(order_id).lower().strip(),
        str(payment_method).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
