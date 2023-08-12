import requests
import datetime

USER_NAME = "shlok12"
TOKEN = "qwertyui"
GRAPH_ID = "graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER_PARAMS = {"token": TOKEN,
               "username": USER_NAME,
               "agreeTermsOfService": "yes",
               "notMinor": "yes"}

# response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

GRAPH_CONFIG = {

    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "shibafu"
}

HEADERS = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_CONFIG, headers=HEADERS)
# print(response.text)

today = datetime.date.today()
DATE = today.strftime("%Y%m%d")

ADD_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
ADD_CONFIG = {
    "date": DATE,
    "quantity": "5.6",
}

# response = requests.post(url=ADD_ENDPOINT, json=ADD_CONFIG, headers=HEADERS)
# print((response.text))

EDIT_ENDPOINT = f"{ADD_ENDPOINT}/{DATE}"
EDIT_CONFIG = {
    "quantity": "3.5"
}

# response = requests.put(url=EDIT_ENDPOINT, json=EDIT_CONFIG, headers=HEADERS)
# print((response.text))

response = requests.delete(url=EDIT_ENDPOINT, headers=HEADERS)
print((response.text))


