# Threat Detection using Pose & FaceMesh
### This project is a real-time computer vision system that detects potential "threat postures" using MediaPipe Pose and FaceMesh, powered by OpenCV. It estimates body joint angles and facial landmarks to assess if a person's posture might indicate a threatening intent, such as arms lowered and face locked on camera.

**🎯 Developed by Abhijeet Singh as a side project, combining creativity and computer vision. Hope you find it intriguing!**


# DEMO:-

![pls wait](https://github.com/abhijeet1592006/threat-detector/blob/main/demo.gif)

# 🧠 Features
- 🎥 Real-time video capture using webcam.

- 🧍 Full-body pose estimation using MediaPipe Pose.

- 🧠 Facial landmark detection using MediaPipe FaceMesh.

  ***🎯 Threat logic: flags user as a “threat” when:***

  Left shoulder angle is significantly lowered.

  Left arm is nearly straight down.

**Eye-level (landmark 151) is directly facing the camera.**

**🚨 Displays "THREAT" message and visual indicators like crosshairs on the face when threat posture is detected.**

# 🧰 Technologies Used
- Python 3

- OpenCV

- MediaPipe (Pose + FaceMesh)

- Math (for angle calculations)


# 📂 Project Structure
```bash

📁 threat-detection
 ┣ 📄 main.py        # Core detection logic
 ┗ 📄 README.md      # You're here!

```
# 🏗️ How It Works
The webcam feed is continuously processed frame by frame.

Pose landmarks are extracted for shoulder, elbow, wrist, and hip.

Facial landmarks are tracked (especially the eyes/forehead region).

If the person’s left arm is down and shoulder is lowered, and their face is in direct view, a "THREAT" label is triggered.

### PLEASE NOTE:- IT IS JUST A PROTOTYPE AND MAY NOT BE ACCURATE, IT IS STILL IN PROGRESS.

# 🖥️ Installation & Usage
**🔧 Prerequisites**
Python 3.6+

pip (Python package installer)

## 📦 Install dependencies
```bash
pip install opencv-python mediapipe
```

## ▶️ Run the program
```bash
python main.py
Press q to quit the window.
```

## 🧮 How Angle is Calculated
Custom angle calculation using vector math and atan2:

```python
=
def findangle(p1, p2, p3):
    return math.degrees(
        math.atan2((p2[1]-p3[1]), (p2[0]-p3[0])) -
        math.atan2((p2[1]-p1[1]), (p2[0]-p1[0]))
    )

```
**This helps estimate elbow and shoulder angles accurately to infer body posture.**


# 📜 License
**This project is licensed under the MIT License.**

#### MIT License

Copyright (c) 2025 Abhijeet Singh


# 🙏 Acknowledgements
**MediaPipe by Google for the Pose & FaceMesh APIs.**

**OpenCV for real-time video processing.**


# 📬 Contact
For suggestions, improvements, or collabs:
📧 abhijeet8800434205@gmail.com
