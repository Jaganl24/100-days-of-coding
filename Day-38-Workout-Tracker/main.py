import requests
from datetime import datetime
from os import environ

# Keys, IDs, passwords and endpoints
APP_ID = environ['APP_ID']
API_KEY = environ['API_KEY']
USERNAME = environ['USERNAME']
PASSWORD = environ['PASSWORD']
TOKEN = environ['TOKEN']
nutrition_ix_endpoint = environ['NUTRI_ENDP']
sheety_endpoint = environ['SHEETY_ENDP']

# variables
WEIGHT = 95
HEIGHT = 195.58
AGE = 24

# config for nutrition API
nutrition_ix_config={
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE,
}

nutrition_ix_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

sheety_headers ={
    "Authorization": TOKEN,
}

# asks user what they did and pushed prompt to config dict
prompt = input("Tell me what workout you did: ")
nutrition_ix_config['query'] = prompt

response_nix = requests.post(url=nutrition_ix_endpoint, json=nutrition_ix_config, headers=nutrition_ix_headers)
data = response_nix.json()
print(data)

# gets todays date and current time
DATE = datetime.today().strftime('%Y/%m/%d')
TIME = datetime.now().strftime("%H:%M:%S")

for items in data['exercises']:

    # gets other exercise info for sheet
    exercise = items['name']
    calories = items['nf_calories']
    duration = items['duration_min']
    # dict setup for google spreadsheet
    workout_data = {
        'workout': {
            'date': DATE,
            'time': TIME,
            'exercise': exercise,
            'duration': f"{duration} min",
            'calories': calories,
        },
    }
    # send info to google sheet
    response_s = requests.post(url=sheety_endpoint, json=workout_data, auth=(USERNAME, PASSWORD), headers=sheety_headers)









