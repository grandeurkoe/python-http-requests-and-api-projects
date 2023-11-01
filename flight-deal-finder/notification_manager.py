import smtplib
import os

# Important twilio AUTH_KEY stored as environment variable
MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]


class NotificationManager:
    def mail_best_offer(self, best_offer):
        """Sends an Email with the best offer available."""
        if best_offer['viaCity'] == "":
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs="testing.meowya@gmail.com", msg=f"Subject:Low price "
                                                                                                 f"alert!\n\nOnly £{best_offer['flightPrice']} from {best_offer['departureCity']}-{best_offer['flyFrom']} to {best_offer['destinationCity']}-{best_offer['flyTo']}, from {best_offer['dateFrom']} to {best_offer['dateTo']}.".encode('utf-8'))
        else:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs="testing.meowya@gmail.com", msg=f"Subject:Low price "
                                                                                                 f"alert!\n\nOnly £{best_offer['flightPrice']} from {best_offer['departureCity']}-{best_offer['flyFrom']} to {best_offer['destinationCity']}-{best_offer['flyTo']}, from {best_offer['dateFrom']} to {best_offer['dateTo']}.\nFlight has {best_offer['stopOver']} stop over, via {best_offer['viaCity']} City.".encode('utf-8'))
