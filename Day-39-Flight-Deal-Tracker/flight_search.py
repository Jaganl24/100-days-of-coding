import requests
from datetime import datetime, timedelta
from os import environ

API_KEY_AMADEUS = environ['API_KEY']
API_SECRET_AMADEUS = environ['API_SECRET_AMADEUS']
URL_AMADEUS = environ['URL_AMADEUS']
URL_CITY_DATA = environ['URL_CITY_DATA']
URL_FLIGHT_SEARCH = environ['URL_FLIGHT_SEARCH']


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = API_KEY_AMADEUS
        self.api_secret = API_SECRET_AMADEUS
        self._token = self._get_new_token()
        self.header = {
            "Authorization": f"Bearer {self._token}"
        }
        self._origin_location_code = 'YVR'
        self.start_date = datetime.today()+timedelta(days=7)
        self.end_date = datetime.today()+timedelta(days=21)

    def _get_city_iata_code(self, city):

        parameters = {
            'keyword': city,
            'max': 2,
            'include': "AIRPORTS"

        }

        response_iata = requests.get(url=URL_CITY_DATA, params=parameters, headers=self.header)
        try:
            iata_code = response_iata.json()['data'][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"

        return iata_code



    def _get_new_token(self):
        # Header with content type as per Amadeus documentation
        header_token = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self.api_secret
        }
        response_token = requests.post(url=URL_AMADEUS, headers=header_token, data=body)
        print(f"your response token is {response_token.json()['access_token']}.\n"
              f"This token expires in {response_token.json()['expires_in']} seconds\n ")
        return response_token.json()['access_token']

    def find_cheapest_flight(self, destination):

        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": self._origin_location_code,
            "destinationLocationCode": destination,
            "departureDate": self.start_date.strftime('%Y-%m-%d'),
            "returnDate": self.end_date.strftime('%Y-%m-%d'),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "CAD",
            "max": "10",
        }

        response = requests.get(
            url=URL_FLIGHT_SEARCH,
            headers=headers,
            params=query,
        )


        try:
            flight_data = response.json()
            data = {

                'cheapest_flight': flight_data['data'][0]['price']['total'],
                'origin': flight_data['data'][0]['itineraries'][0]['segments'][0]['departure']['iataCode'],
                'destination': flight_data['data'][0]["itineraries"][0]["segments"][0]["arrival"]["iataCode"],
                'out_date': flight_data['data'][0]["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0],
                'return_date': flight_data['data'][0]["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                }

        except:

            data_error = {
                'cheapest_flight': 'N/A',
                'origin': 'N/A',
                'destination': 'N/A',
                'out_date': 'N/A',
                'return_date': 'N/A'
            }
            return data_error
        else:
            return data


