# Aerial Object Detection using YOLOv8

This project demonstrates real-time aerial object detection on drone-style videos using the YOLOv8 deep learning model. The videos simulate drone surveillance footage without requiring actual drone hardware.

## Features

Automatically processes all videos placed in the videos/ folder

Detects multiple object classes (people, vehicles, boats, etc.) in each frame

Outputs annotated videos with bounding boxes in the outputs/ folder

Displays live detection preview while processing

Uses Ultralytics YOLOv8 nano model (yolov8n.pt) for fast inference

## Setup Instructions

Clone this repository:
git clone https://github.com/pythondev958/Aerial_Object_Detection_YOLOv8.git
cd Aerial_Object_Detection_YOLOv8

Create and activate a virtual environment:

Windows:
python -m venv venv
venv\Scripts\activate

macOS/Linux:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Add your aerial-style videos to the videos/ folder.

Run the detection script:
python yolo_video_aerial.py
Annotated videos will be saved in the outputs/ folder.

## Sample Drone Footage

The aerial videos used here are from Pixabay, a free stock resource, to simulate drone surveillance footage.

## Skills Demonstrated

Python

Computer Vision

YOLOv8

OpenCV

Video Processing

Object Detection

## License

This project is for educational and non-commercial use.

Feel free to raise issues or contribute via pull requests!
