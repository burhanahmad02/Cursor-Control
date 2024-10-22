# Cursor Control with Hand Landmarks

## Overview

This project implements a real-time cursor control system using hand landmarks detected via a webcam. By leveraging OpenCV and MediaPipe, the project captures and processes video frames to track hand movements and translate them into cursor actions. The system recognizes specific gestures to perform common cursor tasks such as moving, clicking, and dragging.

## Features

- **Real-Time Hand Tracking**: Utilizes MediaPipe's hand landmark detection to track hand movements accurately.
- **Cursor Movement**: Maps hand movements to cursor movements on the screen for intuitive control.
- **Smooth and Responsive**: Provides a smooth and responsive cursor control experience.

## Future Features

- **Click Actions**: Recognizes gestures for left-click and right-click actions.
- **Drag and Drop**: Allows dragging and dropping objects with natural hand gestures.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/burhanahmad02/Cursor-Control.git
   cd Cursor-Control
2. **Install dependencies**:
   ```bash
   -Python 3.x
   -OpenCv
   -MediaPipe
3. **Run Script**:
   ```bash
   python MouseControl.py
## How It Works

- **Click Actions**: The system captures video frames from the webcam and processes them using MediaPipe to detect hand landmarks.
- **Gesture Recognition**: The detected landmarks are analyzed to recognize gestures such as finger positions and hand movements.
- **Cursor Mapping**: Recognized gestures are mapped to corresponding cursor actions, such as movement, clicks, and drags.
- **Execution**: Cursor actions are executed on the operating system, allowing for seamless control.
## Requirements
- Python 3.x
- OpenCV
- MediaPipe
## Future Enhancements
- Adding support for multi-hand tracking.
- Implementing additional gestures for more complex actions.
- Enhancing gesture recognition accuracy.
## Contributions
- Contributions are welcome! Please fork the repository and create a pull request with your improvements.
## License
- This project is licensed under the MIT License.
