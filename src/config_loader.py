# config_loader.py
import json
import logging

def load_config():
    """Loads configuration from config.json.

    Returns:
        dict: Configuration data if successful, otherwise exits the program.
    """
    logging.info("Attempting to load configuration.")
    try:
        with open("config.json", "r") as file:
            config = json.load(file)
            logging.info("Successfully loaded configuration.")
            return config
    except FileNotFoundError:
        logging.critical("Configuration file not found. Please ensure 'config.json' exists.")
        print("Configuration file not found. Please ensure 'config.json' exists.")
        exit(1)
    except json.JSONDecodeError:
        logging.critical("Error reading 'config.json'. Please ensure it contains valid JSON.")
        print("Error reading 'config.json'. Please ensure it contains valid JSON.")
        exit(1)