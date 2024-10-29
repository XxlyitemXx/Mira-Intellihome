from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os
import logging
from config_loader import load_config

language = load_config().get("language")

def text_to_speech(text, lang=language): 
    """Converts text to speech using gTTS and plays the audio.

    Args:
        text (str): Text to convert.
        lang (str, optional): Language code. Defaults to "th".
    """
    logging.info("Attempting text-to-speech conversion.")
    try:
        tts = gTTS(text, lang=lang)
        tts.save("tts.mp3")
        sound = AudioSegment.from_mp3("tts.mp3")
        play(sound)
        os.remove("tts.mp3")
        logging.info("Successfully converted text to speech.")
    except Exception as e:
        logging.error(f"Text-to-speech conversion failed: {e}")