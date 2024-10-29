# webhook_sender.py
import requests
import logging

def send_webhook(content, name_type, url):
    """Sends a message to a Discord webhook.

    Args:
        content (str): Message content.
        name_type (str): Webhook username.
        url (str): Webhook URL.
    """
    data = {
        "content": content,
        "username": name_type
    }
    try:
        result = requests.post(url, json=data)
        result.raise_for_status() # Raise an exception for bad status codes
        logging.info(f"Webhook sent successfully: {content}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to send webhook: {e}")