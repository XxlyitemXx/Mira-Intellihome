import time
import sys
import os

def timer(duration):
    print(f"Timer set for {duration} seconds")
    time.sleep(duration)
    print("Time's up!")

    # Create a file to signal timer expiry
    with open("timer_expired.txt", "w") as f:
        f.write("expired") 

if __name__ == "__main__":
    try:
        duration = int(sys.argv[1]) 
    except (IndexError, ValueError):
        print("Usage: python timer_script.py <duration>")
        sys.exit(1)
    timer(duration)