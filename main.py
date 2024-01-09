import requests
from twilio.rest import Client
STOCK = "IBM"
COMPANY_NAME = "Apple"
KEY = "3BJ81TLSEX1CFV0G"
STOCK_ENDPOINT = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=AAPL&apikey={KEY}"
NEWS_ENDPOINT = f"https://newsapi.org/v2/everything?qInTitle=Apple&language=en&from=2023-02-28&sortBy=publishedAt&apiKey=97071c0863cd42e79b64e0071eb1c6f8"
SID = "AC8c271f6a2c14c2e7140a4a6ecdc8d3ec"
AUTH = "fd03d7ab4fd1f740dd6388fb4eea8509"
PHONE = "+14345955528"


response_stock = requests.get(STOCK_ENDPOINT)
response_stock.raise_for_status()
data_stock = response_stock.json()["Time Series (Daily)"]
day_data = [value for (key, value) in data_stock.items()]
# print(day_data)
response_news = requests.get(NEWS_ENDPOINT)
response_news.raise_for_status()
data_news = response_news.json()["articles"]
# news_list = [value for (key, value) in data_news.items()]


closing_yesterday = float(day_data[0]['4. close'])
closing_before_yesterday = float(day_data[12]['4. close'])
difference = closing_yesterday - closing_before_yesterday

perc = (difference/closing_before_yesterday)*100




client = Client(SID, AUTH)
if perc > 1 or perc < -1:
    for i in range(0, 4):
        message = client.messages.create(

            body=f"\nHeadline:\n {data_news[i]['title']}\n Brief:\n {data_news[i]['description']}",
            from_=PHONE,
            to="+918570810853"
        )



