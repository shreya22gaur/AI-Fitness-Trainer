# 🏋️ AI Fitness Trainer

An AI-powered fitness coaching web application built using **Flask, OpenCV, MediaPipe, and NumPy**. The system analyzes squat posture from uploaded images, calculates knee joint angles using pose estimation, and provides real-time feedback on exercise form.

---

## 🚀 Features

* Upload exercise images through a web interface
* Human pose detection using MediaPipe Pose
* Automatic knee angle calculation
* Squat posture assessment
* Real-time exercise feedback
* User-friendly Flask frontend
* Ready for cloud deployment

---

## 🛠️ Technologies Used

* Python
* Flask
* OpenCV
* MediaPipe Pose
* NumPy
* HTML/CSS

---

## 📂 Project Structure

```text
AI_Fitness_Trainer/
│
├── app.py
├── requirements.txt
├── render.yaml
├── README.md
│
├── templates/
│   └── index.html
│
└── screenshots/
    ├── homepage.png
    ├── good_squat.png
    └── standing_position.png
```

---

## 📸 Screenshots



###  Squat Detection

<img width="903" height="425" alt="image" src="https://github.com/user-attachments/assets/e28d8b8c-0eb2-44c8-9d42-648db1ab2b67" />


### Standing Position Detection

<img width="801" height="429" alt="image" src="https://github.com/user-attachments/assets/4902f0d9-ea9d-4316-a462-aeb5929f801d" />


---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI_Fitness_Trainer.git
```

### Navigate to Project Directory

```bash
cd AI_Fitness_Trainer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User uploads an image containing a person.
2. MediaPipe Pose detects body landmarks.
3. Hip, knee, and ankle coordinates are extracted.
4. Knee joint angle is calculated.
5. Exercise form is evaluated based on the angle.
6. Feedback is displayed instantly.

---

## 📊 Sample Results

### Good Squat

```text
✅ Good Squat
Knee Angle: 85.3°
```

### Needs Improvement

```text
⚠️ Go Lower
Knee Angle: 118.7°
```

### Standing Position

```text
❌ Standing Position
Knee Angle: 172.4°
```

---

## 🎯 Applications

* Personal Fitness Coaching
* Home Workout Assistance
* Exercise Form Analysis
* Sports Performance Monitoring
* Computer Vision Learning Projects

---

## 📈 Key Concepts Demonstrated

* Human Pose Estimation
* Computer Vision
* Geometric Angle Calculation
* Flask Web Development
* Machine Learning Applications in Fitness

---

## 🔮 Future Enhancements

* Real-Time Webcam Analysis
* Squat Rep Counter
* Push-Up Counter
* Bicep Curl Detection
* Workout Tracking Dashboard
* Exercise History Storage
* Multi-Exercise Support
* Mobile Application Integration

---

## 📌 Key Metric

* Accurate pose landmark detection using MediaPipe Pose
* Real-time knee angle computation
* Automated squat form classification

---

## 👩‍💻 Author

**Shreya Gaur**

Machine Learning | Computer Vision | Generative AI

---

⭐ If you found this project useful, please consider giving it a star.
