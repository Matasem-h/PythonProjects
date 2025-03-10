import requests
from datetime import datetime

USERNAME = "matasem"
TOKEN = "juifwe345ijokklmdfs43klm5"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# https://pixe.la/@matasem - My account
# https://pixe.la/v1/users/matasem/graphs/graph1.html My graph

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Push-ups Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2025, month=3, day=9)
print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "30",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

