import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Capture video from webcam
cap = cv2.VideoCapture(0)

# Get screen size
screen_width, screen_height = pyautogui.size()

# Initialize variables for smoothing the cursor movement
num_frames = 5
x_coords = np.zeros(num_frames)
y_coords = np.zeros(num_frames)
frame_index = 0

# Frame rate control
frame_time = 0.03  # 30 ms or approximately 30 FPS

def smooth_coordinates(x, y, x_coords, y_coords, frame_index):
    x_coords[frame_index % num_frames] = x
    y_coords[frame_index % num_frames] = y
    return np.mean(x_coords), np.mean(y_coords)

while cap.isOpened():
    start_time = time.time()

    success, image = cap.read()
    if not success:
        break

    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the frame and detect hands
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the image
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the tip of the index finger
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Convert coordinates to screen space
            x = int(index_finger_tip.x * screen_width)
            y = int(index_finger_tip.y * screen_height)

            # Smooth coordinates
            x, y = smooth_coordinates(x, y, x_coords, y_coords, frame_index)
            frame_index += 1

            # Move mouse cursor
            pyautogui.moveTo(x, y)

    # Display the resulting frame
    cv2.imshow('Hand Tracking', image)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

    # Frame rate control
    elapsed_time = time.time() - start_time
    if elapsed_time < frame_time:
        time.sleep(frame_time - elapsed_time)

cap.release()
cv2.destroyAllWindows()
