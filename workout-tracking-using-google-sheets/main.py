import os
import requests
from datetime import datetime

# Get today's date and time
today_date = datetime.today().date()
today_time = datetime.today().time()

# Important API Keys and Token.
# API keys are stored as environment variables.
NUTRI_APP_ID = os.environ["NUTRI_ID"]
NUTRI_API_KEY = os.environ["NUTRI_KEY"]
SHEETY_USERNAME = os.environ["USERNAME"]
BEARER_TOKEN = os.environ["BEARER_TOKEN"]

# My Workouts  Google Sheet Address - https://docs.google.com/spreadsheets/d/1MDL9iuIWoPxPDKTxJRkEG0EZD4MYpKcm_SetEhMM29E/edit?pli=1#gid=0
# Nutritionix and Sheety Endpoints
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}//myWorkouts/workouts"

# Provide today's exercise data as a string in simple language.
# Request processed data as JSON from Nutritionix API
headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY,
    "x-remote-user-id": "0"
}

nutri_exercise_param = {
    "query": input("Please enter today's exercise entry: ")
}

nutri_response = requests.post(url=NUTRI_ENDPOINT, json=nutri_exercise_param, headers=headers)
sheety_entry = nutri_response.json()

# Add each exercise entry to your Google sheets using the Sheety API.
for entry in sheety_entry["exercises"]:
    sheety_param = {
        "workout": {
            "date": today_date.strftime("%d/%m/%Y"),
            "time": today_time.strftime("%H:%M:%S"),
            "exercise": str.title(entry['name']),
            "duration": entry["duration_min"],
            "calories": entry["nf_calories"],
        }
    }

    sheety_headers = {
        "Authorization": BEARER_TOKEN,
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_param, headers=sheety_headers)
    print(sheety_response.text)
