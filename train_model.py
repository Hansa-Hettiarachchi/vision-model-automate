from ultralytics import YOLO
from pydrive2.auth import GoogleAuth
from pydrive2.auth import ServiceAccountCredentials
from pydrive2.drive import GoogleDrive
import json
import os

# Load the YOLO model
model = YOLO("yolov8m.pt")

# Train the model
model.train(data="/kaggle/working/vision-model-automate/socket_detection-4/data.yaml", epochs=100, imgsz=800, plots=True)

# Save the trained model to Google Drive
model_save_path = "/kaggle/working/runs/train/weights"
model.save(model_save_path)


