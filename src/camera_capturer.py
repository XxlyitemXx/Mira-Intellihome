import cv2
import logging

def realtime_camera():
    """Captures an image from the default webcam and saves it as webcam_shot.jpg."""
    logging.info("Attempting to capture an image from the webcam.")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()  # Release the camera immediately after capturing
    cv2.destroyAllWindows() # Ensure all windows are closed
    if ret:
        cv2.imwrite('webcam_shot.jpg', frame)
        logging.info("Successfully captured and saved webcam image.")
        print("Realtime Image saved")
        return "webcam_shot.jpg" # Return the filename
    else:
        logging.error("Failed to capture image from webcam.")
        print("Failed to get realtime webcam data")
        return None