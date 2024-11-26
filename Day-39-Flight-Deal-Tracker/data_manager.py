import requests
from os import environ

URL_SHEETY = environ['URL_SHEETY']
USERNAME = environ['USERNAME_SHEETY']
PASSWORD = environ['PASSWORD_SHEETY']
TOKEN = environ["TOKEN_SHEETY"]


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.flight_data = {
            'price': {
                'city': "Vancouver",
                'iataCode': "YVR",
                'lowestPrice': 300
            },
        }
        self.header ={
            "Authorization": TOKEN,
        }
        self.destination_data = {}

    # This function reads sheet and returns the cities from the google sheets file, returning it as a dictionary to be used by flight_search
    def read_sheet(self):
        response = requests.get(url=URL_SHEETY, auth=(USERNAME, PASSWORD), headers=self.header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data


