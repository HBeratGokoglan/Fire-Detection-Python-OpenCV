# Fire and Smoke Detection System

## Overview
This project is a **Fire and Smoke Detection System** developed using Python, OpenCV, and email automation tools. It detects fire and smoke through a live camera feed and sends an alert email with the detected image and the current location of the fire. This project is ideal for safety monitoring and early fire detection in various environments.

## Features
- **Real-time Fire and Smoke Detection**: Continuously monitors live camera feed for fire and smoke.
- **Automated Email Alerts**: Sends an email alert with the detected image and location once fire or smoke is detected.
- **Location Tracking**: Fetches the current location (based on IP) and includes it in the email alert.
- **Configurable Parameters**: Adjust detection sensitivity, scale, and brightness via OpenCV trackbars.

## Technologies Used
- **Python**: Main programming language.
- **OpenCV**: Used for real-time video processing and fire/smoke detection.
- **SMTP (Simple Mail Transfer Protocol)**: For sending email alerts.
- **Requests**: To fetch location data using IP address.
- **Cascade Classifier**: Pre-trained XML model for detecting fire and smoke.

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/fire-detection-system.git
    ```
2. **Install the required Python packages**:
    ```bash
    pip install opencv-python requests
    ```

3. **Set up the SMTP configuration**:
   - Replace the placeholder email (`yangingonderme@outlook.com`) and password in the `send_email()` function with your own credentials.
   - Update the recipient email address with the address of the person to be alerted.

## How It Works
1. The system captures a live video feed from the camera.
2. It uses OpenCV's **Cascade Classifier** to detect fire and smoke in real-time.
3. When a fire or smoke is detected, the system:
   - Captures the current frame and saves it as an image.
   - Retrieves the current location based on IP using an external API.
   - Sends an email with the captured image and location to the predefined recipient.
4. The system stops once a predefined detection threshold (e.g., 1000 detections) is reached.

## Code Explanation

### `get_location()`
This function fetches the current location using the [ipinfo.io](https://ipinfo.io/) API, providing the geographical location based on the system's IP address.

### `send_email()`
Sends an email alert with the following:
- A captured image of the detected fire or smoke.
- The current location of the fire (retrieved via IP).

### `fire_detection.py`
The main script:
- Initializes the camera feed.
- Continuously processes frames to detect fire/smoke.
- Draws rectangles around detected fire/smoke.
- If the number of detections exceeds the threshold, it saves the image, sends an email, and exits.

## Configuration
You can customize several parameters for the fire detection system:
- **Camera Resolution**: Adjust the frame width and height in the code.
- **Detection Sensitivity**: Use OpenCV's trackbars to change the scale, neighborhood size, and brightness.
- **Detection Threshold**: Set the number of detections required to trigger an email alert.

## How to Run
1. Ensure that the camera is connected.
2. Run the script:
    ```bash
    python fire_detection.py
    ```
3. Adjust the sensitivity using the trackbars in the window to fine-tune detection.

## Future Improvements
- Integrate support for multiple cameras.
- Implement cloud storage for detected images.
- Add real-time monitoring through a web interface.
- Include sound alarms or notifications on detection.

## License
This project is licensed under the MIT License.

## Acknowledgments
- OpenCV for providing robust image and video processing tools.
- [ipinfo.io](https://ipinfo.io/) for the IP-based location API.
