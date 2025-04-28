# Temple Run Hand Control 

Control **Temple Run** (or similar games) using **hand gestures** through your webcam!  
Built with **Python**, **OpenCV**, **MediaPipe**, and **PyAutoGUI**.

--
## 📋 Features
-  Real-time hand gesture recognition.
- Map hand poses to Temple Run controls:
 - Jump (W key)
 - Slide Down (S key)
- Turn Left (A key)
 - Turn Right (D key)
- Simple and fast performance using MediaPipe
  
--
## 🛠️ Technologies Used
- Python 3
- OpenCV
- MediaPipe
- PyAutoGUI
  
--
## 📥 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/temple-run-hand-control.git
   cd temple-run-hand-control
   
--
Install dependencies:
pip install opencv-python mediapipe pyautogui

--
   Gesture            | Fingers State     | Action    | Key Pressed
   
✋ All fingers up    | [1,1,1,1,1]       | Slide Down | S

☝️ Only index finger up | [0,1,0,0,0]    | Jump       | W

👉 Thumb and pinky up | [1,0,0,0,1]      | Turn Right | D

✌️ Index and middle up | [0,1,1,0,0]     | Turn Left  | A

--
You can easily modify the gestures by changing the finger patterns inside the code.

--


How it Works
Hand Detection:
1)Uses MediaPipe's 21 hand landmarks detection.

2)Finger State Detection:
Compares tip landmark positions to identify open or closed fingers.

3)Gesture Recognition:
Matches detected finger states to predefined game commands.

4)Key Simulation:
PyAutoGUI is used to simulate keyboard presses for Temple Run controls.

--



 Important Notes:
1)Keep your hand visible in the webcam frame.

2)Use in good lighting conditions for accurate detection.

3)Action cooldown time is 1 second to prevent repeated commands.

4)Works best on laptops/desktops with moderate CPU.

--
 Author
Jaswanth Kumar Pola
GitHub: @jaswanthkumarpola






