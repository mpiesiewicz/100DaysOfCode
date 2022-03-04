import datetime
import requests
from datetime import date
from twilio.rest import Client
from credentials import \
    STOCK_API_TOKEN, \
    NEWS_API_TOKEN, \
    TWILLIO_SID, \
    TWILLIO_TOKEN, \
    TWILLIO_PHONE_NUMBER, \
    TO_PHONE_NUMBER


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TODAY = date.today()
YESTERDAY = (TODAY - datetime.timedelta(days=1)).isoformat()
EREYESTERDAY = (TODAY - datetime.timedelta(days=2)).isoformat()

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
URL = 'https://www.alphavantage.co/query'
params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API_TOKEN,
}

request = requests.get(url=URL, params=params)
request.raise_for_status()
stock_data = request.json()

equity = stock_data['Time Series (Daily)']
yesterdays_close = float(equity[YESTERDAY]['4. close'])
ereyesterdays_close = float(equity[EREYESTERDAY]['4. close'])
print(yesterdays_close, ereyesterdays_close)

increase = 100 * ((yesterdays_close - ereyesterdays_close) / ereyesterdays_close)
if increase >= 0:
    increase_emoji = '🔺'
else:
    increase_emoji = '🔻'
print(increase)

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
URL = 'https://newsapi.org/v2/everything'
params = {
    'q': 'TESLA',
    'from': YESTERDAY,
    'sortBy': 'popularity',
    'apikey': NEWS_API_TOKEN,
}

request = requests.get(url=URL, params=params)
request.raise_for_status()
news_data = request.json()
most_popular = news_data['articles'][:3]
print(most_popular)

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

client = Client(TWILLIO_SID, TWILLIO_TOKEN)

if abs(increase) >= 4:
    for headline in most_popular:
        message_body = f"{STOCK}: {increase_emoji}{increase:.2f}%\n" \
                       f"Headline: {headline['title']}\n" \
                       f"Brief: {headline['description']}\n" \
                       f"Link: {headline['url']}"
        print(message_body)
        message = client.messages \
            .create(
                body=message_body,
                from_=TWILLIO_PHONE_NUMBER,
                to=TO_PHONE_NUMBER,
            )
        print(message.status)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file 
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
"""
