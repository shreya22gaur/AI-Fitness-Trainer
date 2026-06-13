from flask import Flask, render_template, request
import cv2
import mediapipe as mp
import numpy as np
import os

app = Flask(__name__)

print("MediaPipe Version:", mp.__version__)

# Create Pose Detector
try:
    pose = mp.solutions.pose.Pose(
        static_image_mode=True,
        min_detection_confidence=0.5
    )
except Exception as e:
    print("MediaPipe Error:", e)
    pose = None


def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(
        c[1] - b[1],
        c[0] - b[0]
    ) - np.arctan2(
        a[1] - b[1],
        a[0] - b[0]
    )

    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180:
        angle = 360 - angle

    return angle


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if pose is None:
        return render_template(
            "index.html",
            result="MediaPipe initialization failed."
        )

    if "image" not in request.files:
        return render_template(
            "index.html",
            result="No image uploaded."
        )

    file = request.files["image"]

    if file.filename == "":
        return render_template(
            "index.html",
            result="Please select an image."
        )

    image_bytes = np.frombuffer(
        file.read(),
        np.uint8
    )

    image = cv2.imdecode(
        image_bytes,
        cv2.IMREAD_COLOR
    )

    if image is None:
        return render_template(
            "index.html",
            result="Invalid image."
        )

    rgb = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    results = pose.process(rgb)

    if not results.pose_landmarks:
        return render_template(
            "index.html",
            result="No person detected."
        )

    landmarks = results.pose_landmarks.landmark

    # Right side body landmarks
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
        feedback = "✅ Good Squat"

    elif angle < 140:
        feedback = "⚠️ Go Lower"

    else:
        feedback = "❌ Standing Position"

    return render_template(
        "index.html",
        result=feedback,
        angle=round(angle, 2)
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
