import json
import logging
import os

def load_chat_history(session_id):
    """Loads chat history from a JSON file. Creates the file if it doesn't exist.

    Args:
        session_id (str): Unique identifier for the chat session.

    Returns:
        list: Chat history, or an empty list if the file is not found or if there is an error loading it.
    """
    history_dir = "chat_history"
    logging.info("Attempting to load chat history.")
    file_path = os.path.join(history_dir, f"chat_history_{session_id}.json")
    if not os.path.exists(history_dir):
        os.makedirs(history_dir)
    if not os.path.exists(file_path):  # Check if the file exists
        logging.info(f"Creating new chat history file: {file_path}")
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump([], f)  # Create an empty JSON file for the new session
            return [] #Return empty list if the file not existed
        except Exception as e: # Handle potential errors during file creation
            logging.error(f"Error creating chat history file: {e}")
            return []

    try: # Try to load the file if it exists or was just created
        with open(file_path, 'r', encoding='utf-8') as f:
            history = json.load(f)
            logging.info(f"Successfully loaded chat history from {file_path}")
            return history
    except (FileNotFoundError, json.JSONDecodeError) as e:  # Handle FileNotFoundError or JSONDecodeError
        logging.error(f"Error loading chat history: {e}")  # Log the error for debugging
        return [] #Return empty list if the file fails to load or decode


def save_chat_history(session_id, history):
    """Saves chat history to a JSON file.

    Args:
        session_id (str): Unique identifier for the chat session.
        history (list): Chat history to save.
    """
    history_dir = "chat_history"
    logging.info("Attempting to save chat history.")
    file_path = os.path.join(history_dir, f"chat_history_{session_id}.json")
    if not os.path.exists(history_dir):
        os.makedirs(history_dir)
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=4, ensure_ascii=False)
        logging.info(f"Successfully saved chat history to {file_path}")
    except Exception as e:
        logging.error(f"Failed to save chat history: {e}")
