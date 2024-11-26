from twilio.rest import Client
from os import environ
SID_TWILIO = environ['SID_TWILIO']
TOKEN_TWILIO = environ['TOKEN_TWILIO']
FROM_NUMBER = environ['FROM_NUMBER']
TO_NUMBER = environ['TO_NUMBER']


class NotificationManager:

    def __init__(self):
        self.account_sid = SID_TWILIO
        self.auth_token = TOKEN_TWILIO
        self.client = Client(self.account_sid, self.auth_token)

    def send_notif(self, price, origin, destination, start_date, end_date):

        message = self.client.messages.create(
            from_=FROM_NUMBER,
            body=f"️Low price alert! Only ${price} to fly from {origin} to {destination}, on {start_date} until {end_date}",
            to=TO_NUMBER
        )
        print(f"message {message.status}\n")
