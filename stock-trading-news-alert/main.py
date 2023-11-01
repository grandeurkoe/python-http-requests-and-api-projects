import requests
import os
from newsapi import NewsApiClient
import smtplib
import datetime as dt
from datetime import timedelta

# Change the STOCK and COMPANY_NAME to whichever stock you want to track.
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

today_datetime = dt.datetime.now()
today_date = today_datetime.date()

YESTERDAY_DATE = today_date - timedelta(days=1)
DAY_BEFORE_YESTERDAY = today_date - timedelta(days=2)

# CLOSE_TIME is time that the stock market closes down.
CLOSE_TIME = "19:59:00"

# Get your own STOCK_API_KEY from https://www.alphavantage.co/support/#api-key
STOCK_API = os.environ["STOCK_API_KEY"]

# Get your own NEWS_API_KEY from https://newsapi.org/
NEWS_API = os.environ["NEWS_API_KEY"]
news_api = NewsApiClient(api_key=NEWS_API)


MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]

stock_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "outputsize": "full",
    "interval": "1min",
    "apikey": STOCK_API,
}
stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

# Get the stock price at close time for both yesterday and day before yesterday.
stock_data_yesterday = stock_data["Time Series (1min)"][f"{YESTERDAY_DATE} {CLOSE_TIME}"]['4. close']
stock_data_day_before_yesterday = stock_data["Time Series (1min)"][f"{DAY_BEFORE_YESTERDAY} {CLOSE_TIME}"]['4. close']

percentage_change = float(stock_data_yesterday) / float(stock_data_day_before_yesterday)

# Calculate the stock price change in percentage between yesterday and day before yesterday.
if percentage_change < 1:
    price_change = round((1 - percentage_change) * 100)
    stock_price_change = f"🔻{price_change}%\n"
else:
    price_change = round((percentage_change - 1) * 100)
    stock_price_change = f"🔺{price_change}%\n"

# If the stock price increases or decreases by a value greater than 5%.
# Send an SMS with the top 3 articles that explains this stock price change.
if price_change >= 0:
    articles = news_api.get_everything(q=COMPANY_NAME, language='en')
    top_3_articles = articles['articles'][0:3]
    sms_format = f"{STOCK}: {stock_price_change}\n"
    for each_article in top_3_articles:
        sms_format += f"Headline: {each_article['title']}\nBrief: {each_article['description']}\n\n"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="testing.meowya@gmail.com", msg=f"Subject:Stock trading "
                                                                                         f"alert!\n\n{sms_format}".encode('utf-8'))
