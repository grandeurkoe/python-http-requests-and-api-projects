from twilio.rest import Client
import os
import requests
import smtplib

# Important twilio AUTH_KEY stored as environment variable
account_sid = "AC4f183a5a3527be369675e890c6f08666"
auth_token = os.environ['AUTH_KEY']

# Important Sheety API key, Sheety username are stored as environment variables.
SHEETY_API = os.environ["SHEETY_AUTH_BEARER"]
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/flightDeals/users"

MY_EMAIL = "again.meowya@gmail.com"
MY_PASSWORD = "iotmldmwjvxqvxgk"


class NotificationManager:
    headers = {
        "Authorization": SHEETY_API
    }

    def sms_best_offer(self, best_offer):
        """Sends an SMS with the best offer available."""
        client = Client(account_sid, auth_token)
        if best_offer['viaCity'] == "":
            message = client.messages.create(
                body=f"Low price alert! Only €{best_offer['flightPrice']} from {best_offer['departureCity']}-{best_offer['flyFrom']} to {best_offer['destinationCity']}-{best_offer['flyTo']}, from {best_offer['dateFrom']} to {best_offer['dateTo']}.",
                from_='+13344686603',
                to='+' + os.environ['MY_CONTACT'],
            )
        else:
            message = client.messages.create(
                body=f"Low price alert! Only €{best_offer['flightPrice']} from {best_offer['departureCity']}-{best_offer['flyFrom']} to {best_offer['destinationCity']}-{best_offer['flyTo']}, from {best_offer['dateFrom']} to {best_offer['dateTo']}.\n"
                     f"Flight has {best_offer['stopOver']} stop over, via {best_offer['viaCity']} City.",
                from_='+13344686603',
                to='+' + os.environ['MY_CONTACT'],
            )
        print(message.status)
        print("Success! SMS sent.")

    def email_best_offer(self, best_offer):
        """Sends an email with the best offer available."""
        customer_response = requests.get(url=SHEETY_ENDPOINT, headers=self.headers)
        customer_response.raise_for_status()
        for each_customer in customer_response.json()['users']:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as notification_connection:
                notification_connection.starttls()
                notification_connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                if best_offer['viaCity'] == "":
                    message = f"Dear {each_customer['firstName']}, \nOnly £{best_offer['flightPrice']} from {best_offer['departureCity']}-{best_offer['flyFrom']} to {best_offer['destinationCity']}-{best_offer['flyTo']}, from {best_offer['dateFrom']} to {best_offer['dateTo']}.\nClick the link below:\n{best_offer['deepLink']}"
                    notification_connection.sendmail(from_addr=MY_EMAIL, to_addrs=each_customer['email'],
                                                     msg=f"Subject:Low price alert!\n\n{message}".encode("utf-8"))
                else:
                    message = f"Dear {each_customer['firstName']}, \nOnly £{best_offer['flightPrice']} from {best_offer['departureCity']}-{best_offer['flyFrom']} to {best_offer['destinationCity']}-{best_offer['flyTo']}, from {best_offer['dateFrom']} to {best_offer['dateTo']}.\nFlight has {best_offer['stopOver']} stop over, via {best_offer['viaCity']} City.\nClick the link below:\n{best_offer['deepLink']}"
                    notification_connection.sendmail(from_addr=MY_EMAIL, to_addrs=each_customer['email'], msg=f"Subject:Low price alert!\n\n{message}".encode("utf-8"))
        print("Success! Email sent.")