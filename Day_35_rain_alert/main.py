from twilio.rest import Client

# 用於驗證自己的身份 -> twilio
account_sid = "account_sid"
auth_token = "account_token"

# 用於驗證自己的身份 -> OpenWeather
api_key = "api_key"

import requests
parameters = {
    "lat":25.052513,
    "lon":121.545664,
    "appid":"api_id",
    "exclude":"current,minutely,daily"
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
whether_data = response.json()

# for i in range(12):
#     if whether_data['hourly'][i]['weather'][0]['id']<700:
#         print(f"{i+1} hour : Bring an umbrella")

will_rain = False
# 取前12小時(0-11)
weather_slice = whether_data['hourly'][:12]
for hour_data in weather_slice:
    weather_condition_code = hour_data['weather'][0]['id']
    if int(weather_condition_code)<700:
        will_rain=True
        # print("Bring an umbrella")

if will_rain:
    # print("Bring an umbrella")

    # 建立twilio 客戶端
    client = Client(account_sid, auth_token)

    # create要send的message
    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an umbrella.☔️",
                        from_='+12166001318',
                        to='phone number'
                    )

    print(message.sid)
    print(message.status)
