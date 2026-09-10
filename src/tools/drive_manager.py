import os
import sys
import json
import mimetypes

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Scopes needed: drive access to inspect read-only folders and upload to 'Tesis para Scrapear Índices'
SCOPES = ["https://www.googleapis.com/auth/drive"]

CONFIG_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "config")
TOKEN_FILE = os.path.join(CONFIG_DIR, "drive_token.json")
CREDENTIALS_FILE = os.path.join(CONFIG_DIR, "drive_client_secret.json")

TARGET_ROOT_FOLDER = "Agente Tesis"
TARGET_WRITE_FOLDER = "Tesis para Scrapear Índices"

READ_ONLY_FOLDERS = [
    "tesis formateadas",
    "tesis final",
    "presentaciones para el sustento",
    "borradores de tesis",
    "planes de tesis"
]

def load_client_config():
    """Load OAuth client config dynamically without hardcoded secrets."""
    # 1. Check local config file
    if os.path.exists(CREDENTIALS_FILE):
        try:
            with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    # 2. Check local application default credentials from environment or Google tools
    vscode_adc = os.path.expandvars(r"%LOCALAPPDATA%\google-vscode-extension\auth\application_default_credentials.json")
    if os.path.exists(vscode_adc):
        try:
            with open(vscode_adc, "r", encoding="utf-8") as f:
                adc_data = json.load(f)
                client_id = adc_data.get("client_id")
                client_secret = adc_data.get("client_secret")
                if client_id and client_secret:
                    return {
                        "installed": {
                            "client_id": client_id,
                            "client_secret": client_secret,
                            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                            "token_uri": "https://oauth2.googleapis.com/token",
                            "redirect_uris": ["http://localhost:8085", "http://localhost"]
                        }
                    }
        except Exception:
            pass

    raise FileNotFoundError(
        f"OAuth client configuration not found. Please place your client credentials JSON in {CREDENTIALS_FILE}."
    )

def get_drive_service(headless_prompt=False):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    creds = None
    
    if os.path.exists(TOKEN_FILE):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        except Exception as e:
            print(f"Error loading token from {TOKEN_FILE}: {e}")
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                print("Refreshing expired Google Drive token...")
                creds.refresh(Request())
                with open(TOKEN_FILE, "w", encoding="utf-8") as token_out:
                    token_out.write(creds.to_json())
            except Exception as e:
                print(f"Token refresh failed: {e}")
                creds = None

        if not creds:
            if headless_prompt:
                print("Authentication required. Please run drive_manager.py directly in your terminal to complete browser login.")
                return None
            print("Opening browser for one-time Google Drive authentication (chihuacoaudaz@gmail.com)...")
            client_config = load_client_config()
            flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
            creds = flow.run_local_server(port=8085, prompt="consent")
            with open(TOKEN_FILE, "w", encoding="utf-8") as token_out:
                token_out.write(creds.to_json())
            print(f"Token saved successfully to {TOKEN_FILE}")

    service = build("drive", "v3", credentials=creds)
    return service

def find_folder(service, folder_name, parent_id=None):
    query = f"mimeType = 'application/vnd.google-apps.folder' and name = '{folder_name}' and trashed = false"
    if parent_id:
        query += f" and '{parent_id}' in parents"
    
    results = service.files().list(q=query, spaces="drive", fields="files(id, name, parents)").execute()
    files = results.get("files", [])
    if files:
        return files[0]
    return None

def create_folder(service, folder_name, parent_id):
    file_metadata = {
        "name": folder_name,
        "mimeType": "application/vnd.google-apps.folder",
        "parents": [parent_id]
    }
    folder = service.files().create(body=file_metadata, fields="id, name").execute()
    print(f"Created folder '{folder_name}' with ID: {folder.get('id')}")
    return folder

def list_files_in_folder(service, folder_id):
    query = f"'{folder_id}' in parents and trashed = false"
    results = service.files().list(
        q=query,
        spaces="drive",
        fields="files(id, name, mimeType, size, modifiedTime, webViewLink)",
        pageSize=100
    ).execute()
    return results.get("files", [])

def scan_read_only_folders(service, root_folder_id):
    print("\n--- Scanning Read-Only Reference Folders ---")
    manifest = {}
    for folder_name in READ_ONLY_FOLDERS:
        folder = find_folder(service, folder_name, parent_id=root_folder_id)
        if folder:
            f_id = folder["id"]
            files = list_files_in_folder(service, f_id)
            print(f"Folder '{folder_name}' (ID: {f_id}): {len(files)} files found.")
            manifest[folder_name] = [
                {
                    "id": f["id"],
                    "name": f["name"],
                    "mimeType": f["mimeType"],
                    "size": f.get("size", "0"),
                    "link": f.get("webViewLink", "")
                } for f in files
            ]
        else:
            print(f"Folder '{folder_name}': Not found under '{TARGET_ROOT_FOLDER}'.")
            manifest[folder_name] = []
            
    summary_path = os.path.join(CONFIG_DIR, "drive_read_only_inventory.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"Inventory saved to {summary_path}")
    return manifest

def upload_file_to_drive(service, local_path, target_folder_id):
    file_name = os.path.basename(local_path)
    # Check if already exists in folder
    query = f"'{target_folder_id}' in parents and name = '{file_name}' and trashed = false"
    existing = service.files().list(q=query, spaces="drive", fields="files(id, name)").execute().get("files", [])
    if existing:
        print(f"File '{file_name}' already exists in target folder (ID: {existing[0]['id']}). Skipping upload.")
        return existing[0]

    mime_type, _ = mimetypes.guess_type(local_path)
    if not mime_type:
        mime_type = "application/octet-stream"

    file_metadata = {
        "name": file_name,
        "parents": [target_folder_id]
    }
    media = MediaFileUpload(local_path, mimetype=mime_type, resumable=True)
    
    print(f"Uploading '{file_name}' to target folder...")
    uploaded = service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id, name, webViewLink"
    ).execute()
    print(f"Successfully uploaded '{file_name}' (ID: {uploaded.get('id')})")
    return uploaded

def sync_scraped_theses_to_drive(service):
    print(f"\n--- Locating Target Root Folder: '{TARGET_ROOT_FOLDER}' ---")
    root_folder = find_folder(service, TARGET_ROOT_FOLDER)
    if not root_folder:
        raise ValueError(f"Root folder '{TARGET_ROOT_FOLDER}' not found in your Google Drive ('chihuacoaudaz@gmail.com'). Please verify the folder name.")

    root_id = root_folder["id"]
    print(f"Found root folder '{TARGET_ROOT_FOLDER}' (ID: {root_id})")

    # Read-only audit
    scan_read_only_folders(service, root_id)

    # Locate or create write target folder
    print(f"\n--- Locating Target Write Folder: '{TARGET_WRITE_FOLDER}' ---")
    target_folder = find_folder(service, TARGET_WRITE_FOLDER, parent_id=root_id)
    if not target_folder:
        print(f"Folder '{TARGET_WRITE_FOLDER}' does not exist inside '{TARGET_ROOT_FOLDER}'. Creating it...")
        target_folder = create_folder(service, TARGET_WRITE_FOLDER, root_id)

    target_id = target_folder["id"]
    print(f"Target upload folder ready: '{TARGET_WRITE_FOLDER}' (ID: {target_id})")

    # Files to upload:
    # 1. Scraped theses from data/scraped_theses
    scraped_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "scraped_theses")
    uploaded_count = 0
    if os.path.exists(scraped_dir):
        for fname in os.listdir(scraped_dir):
            if fname.lower().endswith(".pdf"):
                full_path = os.path.join(scraped_dir, fname)
                upload_file_to_drive(service, full_path, target_id)
                uploaded_count += 1

    # 2. Local benchmark theses and guidelines from inputs
    inputs_dir = os.path.join(os.path.dirname(__file__), "..", "..", "inputs")
    for fname in ["PLAN DE TESIS (3).pdf", "TESIS PARA TURITIN.docx", "PLAN DE TESIS (1).docx"]:
        full_path = os.path.join(inputs_dir, fname)
        if os.path.exists(full_path):
            upload_file_to_drive(service, full_path, target_id)
            uploaded_count += 1

    # 3. Grounding markdown and benchmarks
    benchmarks_dir = os.path.join(os.path.dirname(__file__), "..", "..", "docs", "formateador_indices")
    if os.path.exists(benchmarks_dir):
        for fname in os.listdir(benchmarks_dir):
            if fname.endswith(".md"):
                full_path = os.path.join(benchmarks_dir, fname)
                upload_file_to_drive(service, full_path, target_id)
                uploaded_count += 1

    print(f"\nSync complete! Successfully synchronized files into '{TARGET_WRITE_FOLDER}'.")

if __name__ == "__main__":
    service = get_drive_service()
    if service:
        sync_scraped_theses_to_drive(service)
