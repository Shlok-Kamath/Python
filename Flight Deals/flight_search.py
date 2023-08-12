import requests

API_KEY = "9b2f9aca83msh6b1ce017d52e4c2p1197d5jsn9b8280bc3771"
API_HOST = "skyscanner-api.p.rapidapi.com"
ENDPOINT = "https://skyscanner-api.p.rapidapi.com/v3e/flights/live/search/synced"
CONTENT_TYPE = "application/json"

HEADER = {
    'content-type': CONTENT_TYPE,
    'X-RapidAPI-Key': API_KEY,
    'X-RapidAPI-Host': API_HOST
}

FIGHT_CONFIG = {
    "query": {
        "market": "UK",
        "locale": "en-GB",
        "currency": "INR",
        "queryLegs": [
            {
                "originPlaceId": {
                    "iata": "MAA"
                },
                "destinationPlaceId": {
                    "iata": "BOM"
                },
                "date": {
                    "year": 2023,
                    "month": 9,
                    "day": 20
                },

            }
        ],
        "cabinClass": "CABIN_CLASS_ECONOMY",
        "adults": 1
    }
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.response = requests.post(url=ENDPOINT, json=FIGHT_CONFIG, headers=HEADER)
        print(self.response.text)
        pass

    pass
