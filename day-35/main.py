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


BOT_TOKEN = os.getenv("bot_token")
CHAT_ID = os.getenv("chat_id")

api_key_weather = os.getenv("api_key")
lat = float(os.getenv("lat"))
lon = float(os.getenv("long"))

account_sid = os.getenv("account_sid")
api_key_sid = os.getenv("api_key_sid")
api_key_secret = os.getenv("api_key_secret")
wa_number = os.getenv("wa_number")
twilio_trial = os.getenv("twilio_trial")

api_weather_end_point = "https://api.openweathermap.org/data/2.5/forecast"

api_parameters = {
    "lat": lat,
    "lon": lon,
    "appid": api_key_weather,
    "cnt": 4
}
response = requests.get(
    url=api_weather_end_point,
    params=api_parameters
)
# print(response.status_code)
data = response.json()

will_rain = False

for code in range(len(data["list"])):
    if data["list"][code]["weather"][0]["id"] <= 700:
        will_rain = True

if will_rain:
    send_telegram_message(
        BOT_TOKEN,
        CHAT_ID,
        "Twilio 📉\nTelegram📈")
else:
    print("It is not raining.")
