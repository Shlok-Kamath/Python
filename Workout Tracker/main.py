from datetime import datetime
import requests

APP_ID = "672463b5"
API_KEY = "5f89edb4b349d6e736fbb995bdce82b2"

HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

query = input("Tell me which exercise you did: ")

DATA_CONFIG = {
    "query": query,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=ENDPOINT, json=DATA_CONFIG, headers=HEADER)
print(response.json()["exercises"])

duration = response.json()["exercises"][0]["duration_min"]
now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")
exercise = response.json()["exercises"][0]["user_input"]
calories = response.json()["exercises"][0]["nf_calories"]

SHEETS_ENDPOINT = 'https://api.sheety.co/3d4cd653be66fd5bb03ea5a9c6f30337/copyOfMyWorkouts/workouts'
SHEETS_USERNAME = "shlok_kamath"
SHEETS_PASSWORD = "hello_buddy"
SHEETS_AUTH = (SHEETS_USERNAME, SHEETS_PASSWORD)
SHEETS_CONFIG = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

response1 = requests.post(url=SHEETS_ENDPOINT, json=SHEETS_CONFIG, auth=SHEETS_AUTH)
print(response1.text)
