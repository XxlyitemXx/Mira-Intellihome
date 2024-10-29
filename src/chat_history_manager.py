import json
import logging


def load_chat_history(session_id):
    """Loads chat history from a JSON file.

    Args:
        session_id (str): Unique identifier for the chat session.

    Returns:
        list: Chat history, or an empty list if the file is not found.
    """
    logging.info("Attempting to load chat history.")
    file_path = f"chat_history_{session_id}.json"
    try:
        with open(file_path, 'r') as f:
            history = json.load(f)
            logging.info(f"Successfully loaded chat history from {file_path}")
            return history
    except FileNotFoundError:
        logging.warning(f"Chat history file not found: {file_path}")
        return []


def save_chat_history(session_id, history):
    """Saves chat history to a JSON file.

    Args:
        session_id (str): Unique identifier for the chat session.
        history (list): Chat history to save.
    """
    logging.info("Attempting to save chat history.")
    file_path = f"chat_history_{session_id}.json"
    try:
        with open(file_path, 'w') as f:
            json.dump(history, f, indent=4) # Added indent for readability
        logging.info(f"Successfully saved chat history to {file_path}")
    except Exception as e:
        logging.error(f"Failed to save chat history: {e}")
