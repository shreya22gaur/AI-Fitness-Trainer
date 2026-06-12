from flask import Flask, render_template, request
import cv2
import mediapipe as mp
import numpy as np
import math

app = Flask(__name__)

mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    static_image_mode=True,
    min_detection_confidence=0.5
)

def calculate_angle(a, b, c):

    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(
        c[1]-b[1],
        c[0]-b[0]
    ) - np.arctan2(
        a[1]-b[1],
        a[0]-b[0]
    )

    angle = np.abs(
        radians * 180.0 / np.pi
    )

    if angle > 180:
        angle = 360-angle

    return angle

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["image"]

    image_bytes = np.frombuffer(
        file.read(),
        np.uint8
    )

    image = cv2.imdecode(
        image_bytes,
        cv2.IMREAD_COLOR
    )

    rgb = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    results = pose.process(rgb)

    if not results.pose_landmarks:

        return render_template(
            "index.html",
            result="No Person Detected"
        )

    landmarks = results.pose_landmarks.landmark

    hip = [
        landmarks[24].x,
        landmarks[24].y
    ]

    knee = [
        landmarks[26].x,
        landmarks[26].y
    ]

    ankle = [
        landmarks[28].x,
        landmarks[28].y
    ]

    angle = calculate_angle(
        hip,
        knee,
        ankle
    )

    if angle < 90:
        result = "✅ Good Squat"

    elif angle < 140:
        result = "⚠️ Go Lower"

    else:
        result = "❌ Standing Position"

    return render_template(
        "index.html",
        result=result,
        angle=round(angle, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)