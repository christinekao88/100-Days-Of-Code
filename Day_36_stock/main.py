import requests
from requests.api import patch

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TEILIO_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

#-------------------------------- Alpha Vantage ----------------------------------------#
##### 1. - Get yesterday's closing stock price. #####
alpha_vantage_api_key = "api key"

parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    # "outputsize":"full",
    "apikey":alpha_vantage_api_key,
}
response = requests.get(STOCK_ENDPOINT,params=parameters)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
# print(data.keys())

# 每日收盤價 e.g. [new_value for (key, value) in dictionary.items()]

# for day in data:
#     close_price = data[day]['4. close']
#     print(f"{day} 收盤價 : {close_price}")

# close_price = [data[day]['4. close'] for (day, data) in data.items()]
# yesterday_price = [float(close_price[i+1]) for i in range(len(close_price))]
# before_yesterday_price = [float(close_price[i+2]) for i in range(len(close_price))]
# substract = [abs(yesterday_price[i] - before_yesterday_price[i]) for i in range(len(close_price))]

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

##### 2. - Get the day before yesterday's closing stock price  #####
day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday['4. close']

##### 3. - Find the positive difference between 1 and 2.  #####
difference = abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))

##### 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday. #####
diff_percent = round(difference / float(yesterday_closing_price) *100)

##### 5. - If TODO4 percentage is greater than 5 then print("Get News") #####
up_down = None
if diff_percent>0:
    up_down = "🔺"
else:
    up_down = "🔻"
    # print("Get News")

    #-------------------------------- News API ----------------------------------------#
    ##### 6. use the News API to get articles related to the COMPANY_NAME #####
    news_api_key = "api key"

    news_parameters = {
        "qInTitle":STOCK,
        "apikey":news_api_key,
    }
    news_response = requests.get(NEWS_ENDPOINT,params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()['articles']

    ##### 7. Use Python slice operator to create a list that contains the first 3 articles. #####
    three_articles = articles[:3]

    #####  8. Create a new list of the first 3 article's headline and description using list comprehension. #####
    formatted_articles = [f"{STOCK}:{up_down}{diff_percent}% \n {article} \n Headline : {news['title']}. \n Brief : {news['description']}." for news in three_articles]
    # news_title = [news['title'] for news in three_articles]
    # news__brief = [news['description'] for news in three_articles]
    # print(formatted_articles)

    #-------------------------------- twilio ----------------------------------------#
    ##### 9. - Send each article as a separate message via Twilio.  #####
    from twilio.rest import Client

    # 用於驗證自己的身份 -> twilio
    twilio_sid = "twilio_sid "
    twilio_token = "twilio_token"

    client = Client(twilio_sid, twilio_token)

    # create要send的message
    for article in formatted_articles:
        message = client.messages \
                        .create(
                            body=article,
                            from_='+12166001318',
                            to='phone number'
                        )

        print(message.sid)
        print(message.status)
