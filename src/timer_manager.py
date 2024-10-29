import time
import os
import threading
from tts_speaker import text_to_speech  # Import from your tts module

def timer(duration):
    """Sets a timer for a specified duration and plays a TTS announcement when it expires."""
    print(f"Timer set for {duration} seconds")
    time.sleep(duration)
    print("Time's up!")
    text_to_speech("Timer's up!") # Use the imported text_to_speech function



def check_timer():
    """Continuously checks for a timer expiration file and announces if found."""
    while True:
        if os.path.exists("timer_expired.txt"):
            print("Timer expired! Playing TTS announcement...")
            os.remove("timer_expired.txt") # Remove the file after processing


        time.sleep(1)