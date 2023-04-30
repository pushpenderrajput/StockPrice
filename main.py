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

# STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.
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
# print(closing_yesterday, closing_before_yesterday)
# print(perc)


# STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
# HINT 1: Think about using the Python Slice Operator
client = Client(SID, AUTH)
if perc > 1 or perc < -1:
    for i in range(0, 4):
        message = client.messages.create(

            body=f"\nHeadline:\n {data_news[i]['title']}\n Brief:\n {data_news[i]['description']}",
            from_=PHONE,
            to="+918570810853"
        )

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
