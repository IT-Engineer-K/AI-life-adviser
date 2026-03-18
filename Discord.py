import os
import requests

def send_message(message):
    webhook_url = os.getenv("WEBHOOK_URL")
    if not webhook_url:
        print("Webhook URL is not set")
        return

    payload = {
        "content": message,
        "username": "ほめほめビュッフェ"
    }

    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            print("Message sent to Discord successfully!")
        else:
            print(f"Failed to send message to Discord. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error sending message to Discord: {e}")