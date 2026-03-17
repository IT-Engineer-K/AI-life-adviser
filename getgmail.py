from googleapiclient.discovery import build
from oauth import get_credentials

# 権限（読み取り専用）

def get_gmail_threads(maxResults=5):
    # oauth.py から認証情報を取得
    creds = get_credentials()

    service = build('gmail', 'v1', credentials=creds)
    
    # メッセージ一覧を取得（最新5件）
    results = service.users().messages().list(userId='me', maxResults=maxResults).execute()
    messages = results.get('messages', [])

    emails_summary = ""
    for msg in messages:
        # メッセージの詳細を取得
        msg_detail = service.users().messages().get(userId='me', id=msg['id']).execute()
        snippet = msg_detail.get('snippet') # メールの冒頭部分
        
        # 件名(Subject)を探す
        headers = msg_detail['payload']['headers']
        subject = next(h['value'] for h in headers if h['name'] == 'Subject')
        
        emails_summary += f"件名: {subject}\n内容一部: {snippet}\n---\n"
    
    return emails_summary

# 実行
if __name__ == "__main__":
    print(get_gmail_threads())