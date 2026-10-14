import requests
import os
from dotenv import load_dotenv

load_dotenv()


def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print(message)
    else:
        print(f"Failed to send message: {response.text}")


# Replace with your actual credentials
BOT_TOKEN = os.getenv("bot_token")
CHAT_ID = os.getenv("chat_id")

send_telegram_message(BOT_TOKEN, CHAT_ID, "Hello World from justpython!")
