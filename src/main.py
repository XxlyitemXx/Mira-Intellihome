# main.py

import speech_recognition as sr
import logging
import time
import threading
import os
import json
from datetime import datetime

# Import from modules
from config_loader import load_config
from weather_getter import get_weather
from tts_speaker import text_to_speech
from camera_capturer import realtime_camera
from discord_manager import send_webhook
from timer_manager import timer, check_timer
from chat_history_manager import load_chat_history, save_chat_history
from gemini_interactor import interact_with_gemini, analyze_image
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold


logging.basicConfig(filename='mira.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(threadName)s - %(message)s')

room_mapping = {
    "bedroom": 210,
    "livingroom": 220,
    "kitchen": 230
}

def process_respond(data):
    """Processes the response from Gemini and determines the function type.

    Args:
        data (dict): Data extracted from Gemini's response.

    Returns:
        tuple: Tuple containing the data and function type.
    """

    if "function" in data:
        if data["function"] == "light_toggle":
            if "light_toggle" in data and data["light_toggle"] in ("on", "off") and "location" in data and "context" in data:
                return data, "light_toggle"
        elif data["function"] == "timer":
            if "timer_seconds" in data and "context" in data:
                return data, "timer"
        elif data["function"] == "send_message":
            if "respond" in data and "send_webhook" in data and "context" in data:
                return data, "send_message"

    # Fallback for send_message without explicit "function" field
    if "send_webhook" in data and data["send_webhook"] and "respond" in data and "context" in data:
       return data, "send_message"

    # General response
    if "context" in data: # Check if 'context' key exists before returning
        return data, "general"
    return  None, None



def main():


    config = load_config()
    if not config: # Exit if config loading fails
        return


    api_key_weather = config.get("api_key_weather")
    api_key_gemini = config.get("api_key_gemini")
    city = config.get("city")
    country = config.get("country_code")
    webhook_url = config.get("discord_webhook")

    print("Configs loaded!")
    logging.info("Configs Confirmed.")


    try:
        genai.configure(api_key=api_key_gemini)
        logging.info("Gemini API key has been confirmed.")
    except Exception as e:
        logging.error(f"Failed to configure Gemini API: {e}")
        return  # Exit if Gemini configuration fails


    print("Loading. . . ")
    logging.info("Starting up the application.")



    generation_config = { # Moved generation config here, no need for it to be global
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 1,
        "max_output_tokens": 8192,
        "response_mime_type": "application/json",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-latest",
        generation_config=generation_config,
        safety_settings={
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        },
        system_instruction="""You're Mira , Mira is a smart home voice assistant system for a project name “intelihome” Intellihome is designed to enhance the lives of its users by utilizing artificial intelligence (AI) to process natural language, images, and sounds. This allows users to control various devices within their homes through voice commands and gestures. The system leverages Google's Gemini model, along with OpenCV and other technologies, to accurately perceive and understand user intentions. Intellihome is capable of learning and adapting to individual user behaviors, ensuring a personalized experience. 
                                        Remember to: 
                                                    - Avoid Text formatting Such as bold and more
                                                    - and unnecessary questions such as “What do you want to know about intellihome”, “Do you want to know anything more?” 
                                        Respond to user requests with structured JSON data as follows: * Timer: * context: Your response to the user (e.g., "Alright, I set a 10-minute timer for you.") * function: "timer" * timer_seconds: The duration of the timer in seconds if user using other like minutes just convert it to second (integer) * Device control (e.g., lights): * context: Your response to the user (e.g., "Alright, I turned off the light in your bedroom.") * function: "light_toggle" * light_toggle: "on" or "off" * location: The room or area where the light is located If the user's request doesn't fall into these categories respond with: * context: Your natural language response to the user No response is needed for just "okay". """
    )

    session_id = input("session id: ")
    if session_id == "":
        session_id = f"{datetime.now()}"
    chat_history = load_chat_history(session_id)
    timer_thread = threading.Thread(target=check_timer)
    timer_thread.daemon = True
    timer_thread.start()

    recognizer = sr.Recognizer() # Initialize recognizer outside the loop
    mic = sr.Microphone()  # Initialize microphone outside the loop


    while True:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        date_string = now.strftime("%Y-%m-%d") # Format the date

        if debug_mode == "false":

            with mic as source:
                print("Listening...")
                logging.info("Listening for user input.")

                try:
                    audio = recognizer.listen(source, timeout=5) # Add a timeout to avoid indefinite listening
                except sr.WaitTimeoutError:
                    logging.info("Listening timed out, continuing to next iteration.")
                    continue # Skip to next iteration if no speech detected within timeout

        try:
            if debug_mode == "true":
                text = input(">>>")

            else:
                logging.info("Recognizing speech...")
                text = recognizer.recognize_google(audio, language="th-TH")
                print("You said:", text)
                logging.info(f"User said: {text}")

            if cv_toggle == "true":
                image_path = realtime_camera()
                if image_path:
                    image_analysis = analyze_image(image_path, model)
                    os.remove(image_path)  # Remove the image file after analysis

                else:
                    image_analysis = "Image capture failed." # Clear message if image capture fails
            else:
                image_analysis = "The camera is offline"


            weather_info = get_weather(api_key_weather, city, country)
            extracted_data, raw_response = interact_with_gemini(text, chat_history, model, current_time, date_string, weather_info, image_analysis)


            if extracted_data:
                print(extracted_data.get("context", "No context provided")) # Safely access 'context'

            chat_history.append({"role": "user", "parts": [text]})
            
            function_type = process_respond(extracted_data)[1]  # Get the function type

            if function_type == "light_toggle":
                location_code = room_mapping.get(extracted_data['location'])
                state_code = 1 if extracted_data['light_toggle'] == "on" else 0
                if location_code:  # Check if location_code is not None
                    command = f"1:{location_code}:{state_code}\n" # Corrected command format
                    # ser.write(command.encode()) # Uncomment and implement serial communication
                else:
                    print(f"Invalid location: {extracted_data['location']}")

            elif function_type == "timer":
                print(f"Function: {extracted_data['function']}")
                print(f"Timer seconds: {extracted_data['timer_seconds']}")
                threading.Thread(target=timer, args=(extracted_data['timer_seconds'],)).start()

            elif function_type == "send_message":
                print(f"Function: {extracted_data['function']}")
                print(f"Respond: {extracted_data['respond']}")
                print(f"Send Webhook: {extracted_data['send_webhook']}")

                if extracted_data['send_webhook']:
                    send_webhook(extracted_data['respond'], "Mira", webhook_url)
                    print("Webhook sent successfully!")

            else:  # Print raw response in case of general replies or JSON errors
                print(raw_response)

            if extracted_data and  "context" in extracted_data:  # Check if 'context' key exists
                chat_history.append({"role": "model", "parts": extracted_data['context']})
                save_chat_history(session_id, chat_history)
                logging.info(f"Mira's response: {extracted_data['context']}")

                # Check for context before attempting TTS
                if "context" in extracted_data and extracted_data["context"]:
                    text_to_speech(extracted_data["context"])

            else:
                print("Gemini did not provide a valid response.")
                logging.warning("Gemini did not provide a valid response.")



        except sr.UnknownValueError:
            logging.warning("Could not understand audio.")
            print("Could not understand audio")
        except sr.RequestError as e:
            logging.error(f"Could not request results from Google Speech Recognition: {e}")
            print("Could not request results; {0}".format(e))
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            print("An error occurred:", e)


if __name__ == "__main__":
    debug_mode = input("debug mode (true/false): ")
    cv_toggle = input("camera (true/false): ")
    main()