import os
import requests

# Important Sheety API key, Sheety username are stored as environment variables.
SHEETY_API = os.environ["SHEETY_AUTH_BEARER"]
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/flightDeals/users"


class Customer:
    headers = {
        "Authorization": SHEETY_API
    }

    def add_customer(self):
        print("Welcome to Meowya's Flight Club.\nHere we find the best flight deals and email them to you.")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        confirm_email = input("Type your email again: ")

        if email == confirm_email:
            customer_param = {
                "user": {
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email,
                }
            }
            customer_sheety_response = requests.post(url=SHEETY_ENDPOINT, json=customer_param, headers=self.headers)
            customer_sheety_response.raise_for_status()
            print("Success! Customer added, look forward to the cheapest flight deals.")
