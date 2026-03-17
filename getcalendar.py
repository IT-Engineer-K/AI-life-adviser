import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth import get_credentials

# カレンダーの読み取り権限を指定

def get_calendar_events(maxResults=20):
    # oauth.py から認証情報を取得
    creds = get_credentials()

    try:
        service = build('calendar', 'v3', credentials=creds)

        # 現在時刻を取得 (ISOフォーマット)
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        print('直近の予定{}件を取得中...'.format(maxResults))
        
        # 予定を取得
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=maxResults, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])
        return events


    except HttpError as error:
        print(f'エラーが発生しました: {error}')

if __name__ == '__main__':
    get_calendar_events()