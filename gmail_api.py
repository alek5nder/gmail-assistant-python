import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def gmail_authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('gmail', 'v1', credentials=creds)
    return service

def get_latest_messages(service, max_results=10):
    results = service.users().messages().list(
        userId='me', labelIds=['INBOX'], maxResults=max_results
    ).execute()
    messages = results.get('messages', [])
    return [msg['id'] for msg in messages]

def get_message_content(service, msg_id):
    message = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
    payload = message.get('payload', {})
    parts = payload.get('parts', [])
    data = None

    if 'body' in payload and 'data' in payload['body']:
        data = payload['body']['data']
    else:
        for part in parts:
            if part['mimeType'] == 'text/plain':
                data = part['body']['data']
                break

    import base64
    if data:
        import email
        decoded_bytes = base64.urlsafe_b64decode(data.encode('ASCII'))
        text = decoded_bytes.decode('utf-8')
        return text
    return ""

def add_label(service, msg_id, label_id):
    service.users().messages().modify(
        userId='me',
        id=msg_id,
        body={'addLabelIds': [label_id]}
    ).execute()

def create_label(service, label_name):
    labels = service.users().labels().list(userId='me').execute().get('labels', [])
    for label in labels:
        if label['name'] == label_name:
            return label['id']
    label_body = {
        "name": label_name,
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show"
    }
    label = service.users().labels().create(userId='me', body=label_body).execute()
    return label['id']
