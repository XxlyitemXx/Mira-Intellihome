
# Intellihome - Your AI-Powered Smart Home Companion

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Intellihome is a Python-based smart home system designed to understand and respond to your needs through voice commands.  Powered by Google's Gemini and leveraging computer vision, Intellihome aims to make your life easier and more comfortable.

## Features

* **Natural Language Understanding:** Interact with Mira, your AI assistant, using natural language. Ask questions, set timers, control smart devices (planned), and more.
* **Contextual Awareness:** Mira understands the current time, date, and weather, and can use this information to provide relevant responses.
* **Extensible Functionality:** Designed with a modular architecture, making it easy to add new features and integrations.
* **Camera Integration (Optional):**  Can be configured to capture images and analyze them using Gemini for contextual awareness (e.g., "How many fingers am I holding up?").
* **Discord Integration:** Send messages to a Discord webhook for notifications or remote control.
* **Timer:** Set timers and receive audio notifications when they expire.

## Getting Started

### Prerequisites

* Python 3.7+
* `pip` (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/xXlyitemXx/Mira-Intellihome.git
   cd Mira-Intellihome
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration:**

   * **Create `config.json`:**  Create a `config.json` file in the project's root directory with the following structure:

     ```json
     {
         "api_key_weather": "YOUR_OPENWEATHERMAP_API_KEY",
         "api_key_gemini": "YOUR_GOOGLE_GEMINI_API_KEY",
         "city": "YOUR_CITY_NAME",
         "country_code": "YOUR_COUNTRY_CODE",  // Two-letter country code
         "discord_webhook": "YOUR_DISCORD_WEBHOOK_URL" //Optional
         "language":"YOUR PREFER LANGUAGE" //two letter
     }
     ```
     * Replace placeholders with your actual API keys and location information.

### Running the application
1. navigate to the root of the project folder.
2. run ```python Mira-Intellihome/src/main.py```.

## Usage

1. **Run `main.py`:** 

   ```bash
   python Mira-Intellihome/src/main.py
   ```
2. Follow the prompts to enter session ID, debug mode and enable/disable camera
3. The application will listen for you command if you disable debug mode.
4. If debug mode enabled enter text command via terminal.

**Example Voice Commands:**

* "What time is it?"
* "What's the weather like?"
* "Set a timer for 5 minutes."
* "Send a message to Discord saying 'Hello from Mira!'"


## Project Structure

* `mira_assistant/`: Contains the core Python modules.
    * `camera_capturer.py`: Handles webcam image capture.
    * `chat_history_manager.py`: Manages loading and saving chat history.
    * `config_loader.py`: Loads configuration from `config.json`.
    * `discord_manager.py`: Sends messages to Discord.
    * `gemini_interactor.py`: Handles interaction with the Google Gemini API.
    * `timer_manager.py`: Manages timer functionality.
    * `tts_speaker.py`: Handles text-to-speech.
    * `weather_getter.py`: Fetches weather data.
    * `main.py`: The main application script.
* `requirements.txt`: Lists the project dependencies.
* `README.md`: This file.


## Roadmap

* Enhanced Smart Home Integrations: Direct control of smart devices (lights, thermostats, etc.).
* Improved Computer Vision:  More robust gesture and object recognition.
* User Interface:  A web or mobile interface for configuration and control.
* Multi-language Support: Extend TTS and speech recognition to more languages.


## Contributing

Contributions are welcome! Please fork the repository and create a pull request.


## License

This project is licensed under the MIT License. See `LICENSE` for more information.


## Acknowledgements

* Google Gemini
* OpenWeatherMap API
* OpenCV


