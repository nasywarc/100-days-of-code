import requests
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("x-app-id")
APP_KEY = os.getenv("x-app-key")


nutrition_exercise_api_end_point = "https://app.100daysofpython.dev"
