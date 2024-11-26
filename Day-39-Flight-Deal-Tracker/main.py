from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from os import environ


#creates necessary objects
data_manager = DataManager()
flight_search = FlightSearch()
notif_manager = NotificationManager()
#reads sheet with city and lowest price data
sheet_data = data_manager.read_sheet()

#finds iataCodes for all cities in sheet data and adds a new key:value pair to sheet data to be used later
for items in sheet_data:

     items['iataCode'] = flight_search._get_city_iata_code(items["city"])


#uses flight_search class to lookup cheapest flights from vancouver to cities in updated sheet_data. if it is lower than the lowest price, a text notif is sent
for row in sheet_data:
     flight_info = flight_search.find_cheapest_flight(row['iataCode'])
     if flight_info['cheapest_flight'] == 'N/A':
          print(f"Flight not found for {row['city']}\n")
     else:
          price = flight_info['cheapest_flight']
          print(f"Flight found to {row['city']} for ${price}")
          if float(price) < float(row['lowestPrice']) and price!=0:
               notif_manager.send_notif(price,flight_info['origin'],flight_info['destination'],flight_info['out_date'], flight_info['return_date'])
















