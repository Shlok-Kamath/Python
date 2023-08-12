api_key = "fd93ead886bb8c27f0574f75f6e3a70e"
account_sid = "AC51ee02eeb10a92f47c1d9d29c16204f5"
auth_token = "9e795c10bdc768f93f5764814fe15125"

import requests
from twilio.rest import Client

PARAMETER = {
    "lat": 72.7333,
    "lon": 19.9667,
    "appid": api_key,
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast", params=PARAMETER)

weather_data = response.json()["list"][:12]

for i in weather_data:
    data = i["weather"][0]["id"]
    if data<700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Bring a umbrella",
            from_="+16693568556",
            to="+917020228678"
        )
        break;

