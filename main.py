import requests
import os
from datetime import datetime

PIXELA_USERNAME = "stingzld"
PIXELA_TOKEN = os.environ['PIXELA_TOKEN']

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

GRAPH_ID = "coding-graph"

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")  # yyyyMMdd
date = today_formatted


# # Create User
# user_params = {
#     "token": PIXELA_TOKEN,
#     "username": PIXELA_USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)


# # Create Graph
# graph_params = {
#     "id": GRAPH_ID,
#     "name": "Coding Graph",
#     "unit": "minutes",
#     "type": "int",
#     "color": "shibafu",
#     "timezone": "America/Chicago"
# }
#
# response = requests.post(url=GRAPH_ENDPOINT,
#                          json=graph_params,
#                          headers=HEADERS
#                          )


# # Delete Graph
# response = requests.delete(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}",
#                            headers=HEADERS
#                            )


# # Post a Pixel
# pixel_params = {
#     "date": date,
#     "quantity": "75"
# }
#
# response = requests.post(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}",
#                          json=pixel_params,
#                          headers=HEADERS
#                          )


# # Update a Pixel
# pixel_params = {
#     "quantity": "100"
# }
#
# response = requests.put(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{date}",
#                         json=pixel_params,
#                         headers=HEADERS
#                         )


# Delete a Pixel
response = requests.delete(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{date}",
                           headers=HEADERS
                           )

print(response.status_code)
print(response.text)
