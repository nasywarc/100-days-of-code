import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

APP_ID = os.getenv("x-app-id")
APP_KEY = os.getenv("x-app-key")

nutrition_exercise_api_end_point = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json"
}

exercise_params = {
    "query": "i swam for 3 hours"
}

response = requests.post(
    url=nutrition_exercise_api_end_point,
    headers=headers,
    json=exercise_params,
)

result = response.json()

print(result["exercises"][0])
print(response.status_code)

today = datetime.now().strftime("%d/%m/%Y")
print(today)

today_time = datetime.now().strftime("%H:%M:%S")
print(today_time)

print(result["exercises"][0]['name'])
print(result["exercises"][0]['duration_min'])
print(result["exercises"][0]['nf_calories'])

sheety_api_add_row_end_point = "https://api.sheety.co/41f2f3750fdb17893e78dcb2e75f918a/myWorkouts100DayOfCode/workouts"

sheety_add_params = {
    "workout": {
        "date": today,
        "time": today_time,
        "exercise": result["exercises"][0]["name"],
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"],
    }
}

sheety_headers = {
    "Authorization": f"Bearer {os.getenv('sheety-token')}",
    "Content-Type": "application/json",
}

response_sheety = requests.post(
    url=sheety_api_add_row_end_point,
    headers=sheety_headers,
    json=sheety_add_params,
)

print("Status:", response_sheety.status_code)
print("Response:", response_sheety.text)
print("Payload:", sheety_add_params)

# print(APP_ID, APP_KEY)
