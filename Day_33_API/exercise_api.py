"""  Response code 
https://httpstatuses.com/ 

1XX : Hold on (this is not final)
2XX : Here you go (you should get your data)
3XX : Go away (you don't have no permission)
4XX : You screwed up or the thing you looking for is not exist
5XX : server screwed up

"""
import requests
from datetime import datetime as dt
#------------------------------ iss-now ---------------------------------#
# API endpoint -> url
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# print (response) # <Response [200]>

# Get actual response code , not an object 
# print (response.status_code) # 200

# 利用request return an un-successful status code
response.raise_for_status()

# 取得原始json數據
data = response.json()

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
iss_position = (longitude,latitude)

#------------------------------ sunset sunrise ---------------------------------#
MY_LAT = 51.5
MY_LONG = -0.12

parameters = {
    "lat":MY_LAT ,
    "lng":MY_LONG,
    # 不要把24小時格式格式化成12小時格式
    "formatted":0
}

# 放入必須參數
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)

# 直接格式化參數在endpoint --->  endpoint ?  parameter1_key=value & parameter2_key=value

# https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400


response.raise_for_status()

data = response.json()

# 取小時部分
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
print(sunrise)
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
print(sunset)

time_now = dt.now()
print(time_now.hour)
