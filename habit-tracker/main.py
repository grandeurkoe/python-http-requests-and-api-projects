import requests
import os
from datetime import datetime

date_today = datetime.now()

PIXELA_USER_ENDPOINT = "https://pixe.la/v1/users"

pixela_user_param = {
    "token": os.environ["PIXELA_TOKEN"],
    "username": "grandeurkoe",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Creates a Pixela User Account.
# My Pixela User Account - https://pixe.la/@grandeurkoe
# pixela_response = requests.post(url=PIXELA_USER_ENDPOINT, json=pixela_user_param)
# print(pixela_response.text)

# Creating a Graph.
PIXELA_GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{pixela_user_param['username']}/graphs"

pixela_graph_param = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji",
}

headers = {
    'X-USER-TOKEN': os.environ["PIXELA_TOKEN"]
}

# You need to provide the pixela authentication token for the below lines of code to work. This can be done using
# HTTP Header.
# pixela_graph_response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=pixela_graph_param, headers=headers)
# print(pixela_graph_response.text)

# After compiling the above code go to https://pixe.la/v1/users/grandeurkoe/graphs/graph1.html

# Post a pixel on Graph.
PIXELA_PIXEL_ENDPOINT = f"https://pixe.la/v1/users/{pixela_user_param['username']}/graphs/{pixela_graph_param['id']}"
#
# pixela_pixel_param = {
#     # This will format the date from YYYY-MM-DD to YYYYMMDD
#     "date": date_today.strftime("%Y%m%d"),
#     "quantity": input("How much did you cycle today? "),
# }
#
# pixela_pixel_response = requests.post(url=PIXELA_PIXEL_ENDPOINT, json=pixela_pixel_param, headers=headers)
# print(pixela_pixel_response.text)

# Update a pixel on Graph.
# update_date_pixel = datetime(year=2023, month=10, day=24)
#
# PIXELA_UPDATE_ENDPOINT = f"{PIXELA_PIXEL_ENDPOINT}/{update_date_pixel.strftime('%Y%m%d')}"
#
# pixela_update_param = {
#     "quantity": "1",
# }
#
# pixela_update_pixel_response = requests.put(url=PIXELA_UPDATE_ENDPOINT, json=pixela_update_param, headers=headers)
# print(pixela_update_pixel_response.text)

# Delete a pixel on Graph.
# delete_date_pixel = datetime(year=2023, month=10, day=24)
# 
# PIXELA_DELETE_ENDPOINT = f"{PIXELA_PIXEL_ENDPOINT}/{delete_date_pixel.strftime('%Y%m%d')}"
# 
# pixela_delete_pixel_response = requests.delete(url=PIXELA_DELETE_ENDPOINT, headers=headers)
# print(pixela_delete_pixel_response.text)

