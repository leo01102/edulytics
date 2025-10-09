# sheets_module.py

import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

# --- CONFIGURATION ---
load_dotenv()
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
# this range may need to be adjusted if the sheet structure changes
DATA_RANGE = "Respuestas de formulario 1!A:T" 

def get_credentials():
    """Handles Google API authentication and token management."""
    credentials = None
    
    # check if a token file already exists
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    
    # if no valid credentials, initiate the OAuth flow
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        
        # save the new credentials for the next run
        with open("token.json", "w") as token:
            token.write(credentials.to_json())
            
    return credentials

def fetch_sheet_data(credentials):
    """Fetches data from the specified Google Sheet."""
    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        print(f"Fetching data from spreadsheet ID: {SPREADSHEET_ID}")
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=DATA_RANGE).execute()
        values = result.get("values", [])
        
        print(f"Successfully fetched {len(values)} rows.")
        return values
        
    except HttpError as error:
        print(f"An error occurred while fetching data: {error}")
        return None