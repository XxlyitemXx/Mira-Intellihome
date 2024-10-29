#!/bin/bash

# Navigate to the project directory
cd "$(dirname "$0")"

# Create and activate the virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Uncomment for Windows

# Install the requirements
pip install -r requirements.txt

# Run main.py (assuming it's in ./src)
python ./src/main.py

# Deactivate the virtual environment (optional)
deactivate