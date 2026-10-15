import requests
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

TOKEN = os.getenv("pixela_token")
USERNAME = os.getenv("pixela_username")


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(
#     url=pixela_endpoint,
#     json=user_params,
# )
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
print(graph_endpoint)

headers = {
    "X-USER-TOKEN": TOKEN,
}

graph_params = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "Page",
    "type": "int",
    "color": "kuro",
}

# response = requests.post(
#     url=graph_endpoint,
#     json=graph_params,
#     headers=headers
# )
# print(response.text)

graphID = graph_params["id"]
pixel_post_endpoint = f"{graph_endpoint}/{graphID}"

print(pixel_post_endpoint)

today = datetime(year=2026, month=10, day=14)
today_formatted = today.strftime("%Y%m%d")

pixel_post_params = {
    "date": today_formatted,
    "quantity": "3",
}

# response = requests.post(
#     headers=headers,
#     url=pixel_post_endpoint,
#     json=pixel_post_params
# )
# print(response.text)

pixel_update_endpoint = f"{pixel_post_endpoint}/{today_formatted}"
print(pixel_update_endpoint)

pixel_update_params = {
    "quantity": "2",
}

# response = requests.put(
#     url=pixel_update_endpoint,
#     headers=headers,
#     json=pixel_update_params,
# )
# print(response.text)

pixel_delete_endpoint = pixel_update_endpoint

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)
