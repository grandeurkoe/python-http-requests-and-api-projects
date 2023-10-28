import os
import requests

# Flight Deal Sheet Address - https://docs.google.com/spreadsheets/d/1JGbWkKxqX3184LsOQz_MmbtWu0h7bk0dadPbejZEg_o/edit#gid=115427991
# Important Sheety API key, Sheety username are stored as environment variables.
SHEETY_API = os.environ["SHEETY_AUTH_BEARER"]
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/flightDeals/prices"


class DataManager:

    headers = {
        "Authorization": SHEETY_API
    }

    def get_sheety_data(self):
        """Retrieves column_name data from Google Sheet. Returns column_name data."""
        column_response = requests.get(url=SHEETY_ENDPOINT, headers=self.headers)
        column_response.raise_for_status()
        sheety_data = column_response.json()['prices']
        return sheety_data

    def update_column(self, column, column_name):
        """Updates column_name data in the Google Sheet."""

        object_id = 2
        for each_entry in range(len(column)):
            column_endpoint = f"{SHEETY_ENDPOINT}/{id}"
            column_param = {
                "price": {
                    column_name: column[each_entry]
                }
            }
            column_response = requests.put(url=column_endpoint, json=column_param, headers=self.headers)
            object_id += 1
