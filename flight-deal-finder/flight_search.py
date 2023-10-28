import os
import requests
from datetime import datetime

# Important Tequila API is stored as environment variables.
FLIGHT_SEARCH_API = os.environ["FLIGHT_API_KEY"]
FLIGHT_LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"

today_date = datetime.today().date()
today_day = today_date.day
today_month = today_date.month
today_year = today_date.year


class FlightSearch:
    headers = {
        "apikey": FLIGHT_SEARCH_API,
    }

    def get_iata_code(self, locations, location_type):
        """Searches IATA code for locations based on location_type. Returns the IATA code"""
        iata_code = []

        for each_entry in locations:
            iata_param = {
                "term": each_entry,
                "location_types": location_type,
            }
            iata_response = requests.get(url=FLIGHT_LOCATION_ENDPOINT, params=iata_param, headers=self.headers)
            iata_response.raise_for_status()
            iata_code.append(iata_response.json()['locations'][0]['code'])
        return iata_code

    def get_cheapest_flight(self, current_city_iata, destination_cities_iata, lowest_prices, departure_city, cities):
        """Gets cheapest flight from the departure city to every destination city in Google Sheet. Returns cheapest
        flight data."""
        flights = []
        via_city = ""
        stop_over = 0

        date_from = datetime(year=today_year, month=today_month, day=today_day + 1).strftime("%d/%m/%Y")

        if (today_month + 6) > 12:
            date_to_month = (today_month + 6) - 12
            date_to_year = today_year + 1

        date_to = datetime(year=date_to_year, month=date_to_month, day=today_day + 1).strftime("%d/%m/%Y")

        for each_destination in range(0, len(destination_cities_iata)):

            flight_search_param = {
                "fly_from": current_city_iata,
                "fly_to": destination_cities_iata[each_destination],
                "date_from": date_from,
                "date_to": date_to,
                "max_stopovers": f"{stop_over}",
                "sort": "price",
                "limit": "1",
            }

            try:
                flight_search_response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, params=flight_search_param,
                                                      headers=self.headers)
                flight_search_response.raise_for_status()
                all_flights = flight_search_response.json()['data'][0]
            except IndexError:
                stop_over += 1
                flight_search_param = {
                    "fly_from": current_city_iata,
                    "fly_to": destination_cities_iata[each_destination],
                    "date_from": date_from,
                    "date_to": date_to,
                    "max_stopovers": f"{stop_over}",
                    "sort": "price",
                    "limit": "1",
                }
                flight_search_response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, params=flight_search_param,
                                                      headers=self.headers)
                flight_search_response.raise_for_status()
                all_flights = flight_search_response.json()['data'][0]
                via_city = all_flights['route'][0]['cityTo']
            finally:
                cheapest_flight_cost = lowest_prices[each_destination]
                cheapest_flight_from = ""
                cheapest_flight_to = ""
                cheapest_destination_city = cities[each_destination]
                cheapest_flight_date_to = date_from

                if cheapest_flight_cost > all_flights['price']:
                    cheapest_flight_cost = all_flights['price']
                    cheapest_flight_from = all_flights['flyFrom']
                    cheapest_flight_to = all_flights['flyTo']
                    cheapest_flight_date_to = all_flights['local_departure'].split('T')[0]
                cheapest_flights = {
                    'flyFrom': cheapest_flight_from,
                    'flyTo': cheapest_flight_to,
                    'departureCity': departure_city,
                    'destinationCity': cheapest_destination_city,
                    'flightPrice': cheapest_flight_cost,
                    'dateFrom': datetime(year=today_year, month=today_month, day=today_day + 1).strftime("%Y-%m-%d"),
                    'dateTo': cheapest_flight_date_to,
                    'viaCity': via_city,
                    'stopOver': stop_over,
                }
                flights.append(cheapest_flights)
        return flights
