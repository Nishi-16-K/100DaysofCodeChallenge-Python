import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = "--Your twilio account sid--"
auth_token = "--Your twilio account auth_token--"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "--Your Stock_Endpoint API KEY--"
NEWS_API_KEY = "--Your News_Endpoint API Key--"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params= {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before = data_list[1]
day_before_closing = day_before["4. close"]

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

difference = float(yesterday_closing_price)-float(day_before_closing)
up_down = None
if difference> 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = (difference/float(yesterday_closing_price)) * 100
print(diff_percent)
if abs(diff_percent)>1:
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles =  news_response.json()["articles"]
    three_articles = articles[:3]


    formatted_article = [f"{STOCK_NAME}: {up_down}{diff_percent}%\n Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_="--Your Twilio account virtual number--",
            to="--Your phone number--"
        )
