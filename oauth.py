import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# デフォルトのスコープ（カレンダーとGmailの両方）
DEFAULT_SCOPES = [
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/gmail.readonly'
]

TOKEN_FILE = 'token.json'
CREDENTIALS_FILE = 'credentials.json'

def get_credentials():
    scopes = DEFAULT_SCOPES
    
    creds = None
    # 既存のトークンを確認
    if os.path.exists(TOKEN_FILE):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, scopes)
        except Exception:
            creds = None
    
    # トークンが無効またはスコープが足りない場合
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception:
                # リフレッシュ失敗時は再度ログイン
                creds = None
        
        if not creds or not creds.valid:
            if not os.path.exists(CREDENTIALS_FILE):
                raise FileNotFoundError(f"{CREDENTIALS_FILE} が見つかりません。")
                
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, scopes)
            creds = flow.run_local_server(port=0)
            
        # 次回のために保存
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
            
    return creds

if __name__ == '__main__':
    # 動作確認：両方のスコープで認証を取得
    try:
        get_credentials()
        print("認証に成功しました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
