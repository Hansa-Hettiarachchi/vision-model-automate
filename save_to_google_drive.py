from pydrive2.auth import GoogleAuth
from pydrive2.auth import ServiceAccountCredentials
from pydrive2.drive import GoogleDrive
import json

# Upload the model file to Google Drive
file_path = "/kaggle/working/runs/train/weights/best.pt"

# Path to the service account key file
SERVICE_ACCOUNT_FILE = 'service_account.json'

# Define the scope
SCOPES = ['https://www.googleapis.com/auth/drive']

# Authenticate using the service account
with open(SERVICE_ACCOUNT_FILE) as f:
    sa_info = json.load(f)

credentials = ServiceAccountCredentials.from_json_keyfile_dict(sa_info, SCOPES)

gauth = GoogleAuth()
gauth.credentials = credentials

drive = GoogleDrive(gauth)

# Create a new folder
folder_metadata = {
    'title': 'Test model',
    'mimeType': 'application/vnd.google-apps.folder',
    'parents': [{'id': '1J9Rgtpd4Tyht9n61u9eLwf2cYNG4rhj0'}]  # Replace with the shared folder ID
}
folder = drive.CreateFile(folder_metadata)
folder.Upload()
print(f'Created folder with ID: {folder["id"]}')

# Create and upload a text file to the newly created folder
file_metadata = {
    'title': 'model_1.pt',
    'parents': [{'id': folder['id']}]  # Specify the folder ID to upload the file into
}
file = drive.CreateFile(file_metadata)
file.SetContentFile(file_path)
file.Upload()
print(f'Uploaded file with ID: {file["id"]}')
