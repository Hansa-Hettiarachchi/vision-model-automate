from ultralytics import YOLO
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Authenticate Google Drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)

# Load the YOLO model
model = YOLO("yolov8n.pt")

# Train the model
model.train(data="/kaggle/working/datasets/data.yaml", epochs=100, imgsz=800, plots=True)

# Save the trained model to Google Drive
model_save_path = "/kaggle/working/runs/train/weights"
model.save(model_save_path)

# Upload the model file to Google Drive
file_path = "/kaggle/working/runs/train/weights/best.pt"
file = drive.CreateFile({'title': 'best.pt'})  # Change the title if needed
file.SetContentFile(file_path)
file.Upload()
