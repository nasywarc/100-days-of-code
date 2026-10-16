import requests
import os
from dotenv import load_dotenv

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
    "query": "today i ran for 20 minutes"
}

response = requests.post(
    url=nutrition_exercise_api_end_point,
    headers=headers,
    json=exercise_params,
)

result = response.json()

print(result["exercises"][0])
print(response.status_code)

# print(APP_ID, APP_KEY)
