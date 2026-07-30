from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("u-100", "email"): {
        "sent": True,
        "delivery_id": "NOTIF-1001",
        "channel": "email",
        "recipient": "maria@company.com",
    },
    ("u-100", "slack"): {
        "sent": True,
        "delivery_id": "NOTIF-1002",
        "channel": "slack",
        "recipient": "@maria.garcia",
    },
    ("u-200", "email"): {
        "sent": True,
        "delivery_id": "NOTIF-1003",
        "channel": "email",
        "recipient": "john@company.com",
    },
    ("u-300", "email"): {
        "sent": True,
        "delivery_id": "NOTIF-1004",
        "channel": "email",
        "recipient": "locked.user@company.com",
    },
    ("u-400", "email"): {
        "sent": True,
        "delivery_id": "NOTIF-1005",
        "channel": "email",
        "recipient": "admin@company.com",
    },
    ("u-400", "slack"): {
        "sent": True,
        "delivery_id": "NOTIF-1006",
        "channel": "slack",
        "recipient": "@alex.admin",
    },
    ("u-500", "email"): {
        "sent": True,
        "delivery_id": "NOTIF-1007",
        "channel": "email",
        "recipient": "disabled@company.com",
    },
}


@tool()
def send_notification(user_id: str, channel: str, message: str):
    """
    Sends a notification to a user via the specified channel.

    Args:
        user_id: The user's ID (e.g. "U-100").
        channel: The notification channel ("email" or "slack").
        message: The notification message content.

    Returns:
        Notification delivery result including delivery_id and recipient, or None if delivery failed.
    """
    key = (
        str(user_id).lower().strip(),
        str(channel).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
