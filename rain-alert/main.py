import requests
import os

# the twilio library allows us to send SMS.
from twilio.rest import Client

# Get your own OpenWeather API by creating a free account at "https://openweathermap.org/"
# API Keys are required to make API Requests to the OpenWeather API.
# os.environ[key] allows you to get the value of the environment variable i.e., key
API_KEY = os.environ['API_KEY']
MY_LAT = 19.194550
MY_LON = 73.190819
is_raining = False

# You need account_sid and auth_token to send SMS using the twilio library.
account_sid = "AC4f183a5a3527be369675e890c6f08666"
auth_token = os.environ['AUTH_KEY']

rain_param = {
    'lat': MY_LAT,
    'lon': MY_LON,
    'exclude': 'current,minutely,daily,alerts',
    'appid': API_KEY,
}

rain_response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=rain_param)

# If the requests.get() function generates 401 Errors, look into whether the onecall version 2.8 is still
# accessible to free OpenWeather Accounts.
rain_response.raise_for_status()

rain_data = rain_response.json()

rain_data_hourly = rain_data['hourly']

for hourly_index in range(0, 12):
    if rain_data_hourly[hourly_index]['weather'][0]['id'] < 700:
        is_raining = True
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body="It's going to rain today. Remember to bring an ☔.",
            from_='+13344686603',
            to= '+' + os.environ['MY_CONTACT']
        )

        print(message.status)
        break

if is_raining is False:
    print("Don't bring Umbrella.")
