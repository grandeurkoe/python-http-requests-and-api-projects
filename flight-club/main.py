from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from customer_acquisition import Customer

DEPARTURE_CITY = "London"
CITIES = []
LOWEST_PRICES = []

flight_sheet_data = DataManager()
flight_search = FlightSearch()
flight_structure_data = FlightData()
flight_notification = NotificationManager()
customer = Customer()
is_looping = True


while is_looping:
    print('''

    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░▒▒▒▒▒▒░▒▒▒░░░▒▒▒░░░▒▒▒▒░░▒▒▒░▒▒▒░▒▒▒▒▒░░░░░▒▒▒▒░░▒▒░░░▒▒▒░▒▒▒░▒▒▒▒▒▒░░░░░░░░░░
    ░░░░░░░░░░░░██▓▓▓▒▓██░░░▒██░░▓██▓▓▓░▒██▒▒██▒▒▓██▓▓░░░░▓██▓▓░▓█▓░░░██▒░▓█▓░██▓▓██▒░░░░░░░░░
    ░░░░░░░░░░░▒██▒░░░██▓░░░▓█▓░██▓░░░░░▓█▓░▓█▓░░▓██░░░░░▓█▓░░░▒██▒░░▓██░▒██▒▒██▒▒██░░░░░░░░░░
    ░░░░░░░░░░░▓████▒▒██▒░░▒██▒▓██░▓██▓▒██████▒░░██▓░░░░▒██░░░░▓██░░░██▓░▓█▓░▓█████░░░░░░░░░░░
    ░░░░░░░░░░▒██▒░░░▓█▓░░░▓█▓░██▓░▒██░▓█▓░▓██░░▒██▒░░░░▓█▓░░░░██▓░░▒██░▒██▒▒██▒▒██▒░░░░░░░░░░
    ░░░░░░░░░░▓██░░░▒██▓▒▒▒██▒░██▓▒▓█▓░██▒░██▓░░▓█▓░░░░░▓██▒▒░▓██▓▒░▓██▒▓█▓░▓██▒▓██░░░░░░░░░░░
    ░░░░░░░░░░▓▓▒░░░▒▓▓▓▓░▒▓▓░░░▒▓▓▓▓▒▒▓▓░▒▓▓░░░▓▓▒░░░░░░▓▓▓▓░▓▓▓▓▓░░▓▓▓▓▒░░▓▓▓▓▓▒░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ''')

    print(f"Menu\n1. Add customer.\n2. Get cheapest flight deals.\n3. Send SMS.\n4. Send Email.\n5. Exit")
    menu_select = int(input("Pick a choice: "))

    if menu_select == 1:
        customer.add_customer()
    elif menu_select == 2:
        sheety_data = flight_sheet_data.get_sheety_data()
        for each_entry in sheety_data:
            CITIES.append(each_entry['city'])
            LOWEST_PRICES.append(each_entry['lowestPrice'])

        iata_codes = flight_search.get_iata_code(CITIES, 'city')
        departure_iata_code = flight_search.get_iata_code([DEPARTURE_CITY], 'city')

        # This was used to set IATA codes for cities in Sheety.
        # flight_sheet_data.update_column(iata_codes, 'iataCode')

        cheapest_flights = flight_search.get_cheapest_flight(departure_iata_code, iata_codes, LOWEST_PRICES,
                                                             DEPARTURE_CITY, CITIES)
        best_offer = flight_structure_data.get_best_offer(cheapest_flights)
        print(f"Cheapest Flight Deal: {best_offer}")
    elif menu_select == 3:
        flight_notification.sms_best_offer(best_offer)
    elif menu_select == 4:
        flight_notification.email_best_offer(best_offer)
    elif menu_select == 5:
        is_looping = False
    else:
        print("Invalid choice.")
