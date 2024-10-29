# response_processor.py

def process_respond(data):
    """Processes the JSON response from the language model.

    Args:
        data (dict): The JSON data from the model.

    Returns:
        tuple: A tuple containing the processed data and the function type.
               Returns (data, "general") if no specific function is identified.
    """
    if "function" in data:
        if data["function"] == "light_toggle":
            if "light_toggle" in data and data["light_toggle"] in ("on", "off"):
                if "location" in data and "context" in data:
                    return data, "light_toggle"
        elif data["function"] == "timer":
            if "timer_seconds" in data and "context" in data:
                return data, "timer"
        elif data["function"] == "send_message":
            if "respond" in data and "send_webhook" in data and "context" in data:
                return data, "send_message"
    if "send_webhook" in data and data["send_webhook"]:
        if "respond" in data and "context" in data:
            return data, "send_message"
    if "context" in data:
        return data, "general"