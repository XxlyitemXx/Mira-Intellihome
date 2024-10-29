import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import json
import logging
from camera_capturer import realtime_camera

def analyze_image(file_path, model):
    """Analyzes an image using the provided Gemini model.

    Args:
        file_path (str): Path to the image file.
        model (google.generativeai.GenerativeModel): Gemini model instance.

    Returns:
        str: Analysis result, or an error message if analysis fails.
    """
    try:
        file = genai.upload_file(path=file_path, display_name="Realtime camera")

        context = model.generate_content([file, "explain what did you see in the picture?"])
        return context.text
    except Exception as e:
        logging.error(f"Image analysis failed: {e}")
        return "Image analysis failed."



def interact_with_gemini(text, chat_history, model, current_time, date, weather_info, image_analysis):
    """Interacts with the Gemini API.

    Args:
        text (str): User input text.
        chat_history (list): History of the conversation.
        model (google.generativeai.GenerativeModel): Gemini model instance.
        current_time (str): Current time.
        date (str): Current date.
        weather_info (str): Current weather information.
        image_analysis (str): Result of image analysis.


    Returns:
        tuple: Tuple containing the structured data, function type, and raw response text.
    """
    chat_session = model.start_chat(history=chat_history)

    prompt = f"""Input: "{text}" 
    Information (Tell this information only when the user asks for it): 
    The time right now is {current_time}. 
    The date is {date}. 
    The weather is {weather_info}. 
    You currently see in the real-time camera: "{image_analysis}"
    """
    response = chat_session.send_message([prompt])


    try:
        structured_data = json.loads(response.text)

    except json.JSONDecodeError:
        structured_data = {"context": response.text} # Handle cases where the response isn't JSON

    return structured_data, response.text
