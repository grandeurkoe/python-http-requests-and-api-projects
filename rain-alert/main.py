import requests
import os
import smtplib

# Get your own OpenWeather API by creating a free account at "https://openweathermap.org/"
# API Keys are required to make API Requests to the OpenWeather API.
# os.environ[key] allows you to get the value of the environment variable i.e., key
API_KEY = os.environ['API_KEY']
MY_LAT = 58.416740
MY_LON = 39.111390
is_raining = False

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]

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

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="testing.meowya@gmail.com", msg="Subject:Rain "
                                                                                             "alert!\n\nIt's going to"
                                                                                             " rain today. Remember "
                                                                                             "to bring an ☔.".encode("utf-8"))

        break

if is_raining is False:
    print("Don't bring Umbrella.")
