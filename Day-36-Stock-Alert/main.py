import requests
import datetime as datetime, timedelta
from twilio.rest import Client
from os import environ


#Whatsapp setup
account_sid = environ['account_sid']
auth_token = environ['auth_token']
client = Client(account_sid, auth_token)

#parameter setup
STOCK = "NVDA"
COMPANY_NAME = "NVIDIA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# getting relevant dates
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
day_before_yesterday = today - datetime.timedelta(days=2)

today_key = today.strftime('%Y-%m-%d')
day_before_yesterday_key = day_before_yesterday.strftime('%Y-%m-%d')
yesterday_key = yesterday.strftime('%Y-%m-%d')

#setting up api parameters
paramaters={
    'stock_api':
        {
            'apikey': environ['apikey_stock'],

            'symbol': STOCK,
            'function': 'TIME_SERIES_DAILY',
    },
    'news_api':
        {
            'apiKey': environ['apikey_news'],
            'qInTitle': COMPANY_NAME + ' stock',
            'sortBy': 'relevancy',
            'pageSize': 3,
            'language': 'en',
            'from':day_before_yesterday_key,
            'to': today_key
    },

}
# Get stock information
stock_data = requests.get(url=STOCK_ENDPOINT, params=paramaters['stock_api'])
yesterday_close_price= float(stock_data.json()['Time Series (Daily)'][yesterday_key]["4. close"])
day_before_yesterday_close_price = float(stock_data.json()['Time Series (Daily)'][day_before_yesterday_key]["4. close"])


# calculate price difference and roudn value to 2 decimal places
price_difference = round(((yesterday_close_price-day_before_yesterday_close_price)/day_before_yesterday_close_price)*100, 2)

# sets symbol for text notif based on price up or down
if price_difference < 0:
    symbol = '🔻'
else:
    symbol = '🔺'

# if the abs value is greater than 5%, fetch news info and send it to phone
if abs(price_difference) > 4:

    # get news information
    news_data = requests.get(url=NEWS_ENDPOINT, params=paramaters['news_api'])
    news_data.raise_for_status()
    articles = news_data.json()['articles']

    # send texts
    for index in range(0, paramaters['news_api']['pageSize']):
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f"️{STOCK}: {symbol}{abs(price_difference)}%\nHeadline: {articles[index]['title']}\nBreif: {articles[index]['description']}\nLink: {articles[index]['url']}",
            to='whatsapp:+17789525383'
        )

