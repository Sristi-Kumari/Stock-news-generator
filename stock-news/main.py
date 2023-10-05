
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API="DK0CM5G8EEBAZH0U"




import requests
from twilio.rest import Client

parameters={
"function": "TIME_SERIES_DAILY",
"symbol": STOCK_NAME,
"apikey":STOCK_API,

}
response=requests.get(STOCK_ENDPOINT,params=parameters)
response.raise_for_status()
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yesterday=data_list[0]
y=yesterday["4. close"]

day_before_yesterday=data_list[1]
d=day_before_yesterday["4. close"]



diff = float(d) - float(y)


percent= (float(diff)/float(y)) * 100


if percent > 1:



    NEWS_API = "67e0292e7ff54403a1b784b13de3f9ae"
    news_parameters = {

        'apiKey': NEWS_API,
        'qInTitle':COMPANY_NAME,
    }


    response2 = requests.get(NEWS_ENDPOINT, params= news_parameters)
    articles=response2.json()["articles"]



    three_articles=articles[:3]
    print(three_articles)







    headline=[f"Headline:{articles['title']}. \nBrief: {articles['description']}" for articles in three_articles]



    twilio_ID="AC699dc1ef421078dfd56c9f37029bcc21"
    twilio_Auth_token="150242bb4d34089a381659576f78605c"
    client=Client(twilio_ID,twilio_Auth_token)
    for articles in headline:
        message=client.messages.create(
        body=articles,
        from_= "+17125814891",
        to="+917301399115",
        )




