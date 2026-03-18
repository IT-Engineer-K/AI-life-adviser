from getgmail import get_gmail_threads
from getcalendar import get_calendar_events
from gemini import Chat
from Discord import send_message

def generate_compliment():
    emails_summary = get_gmail_threads(maxResults=8)
    calendars_events = get_calendar_events(maxResults=100)
    calendars_summary = ''
    for event in calendars_events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        calendars_summary += f"{start} - {event['summary']}\n"

    emails_prompt = "ユーザーの情報拾った上で、ユーザーを心から褒めてください。"
    
    prompt = "直近のメールは以下の通りです。\n" + (emails_summary)
    prompt += "\n"
    prompt += "直近のスケジュールは以下の通りです。\n" + (calendars_summary)

    chat = Chat(emails_prompt)
    chat_response = chat.generate(prompt)
    return chat_response

compliment = generate_compliment()
send_message(compliment)