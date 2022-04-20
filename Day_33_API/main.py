import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 25.051430 # Your latitude
MY_LONG = 121.544044 # Your longitude
MY_EMAIL = "your email"
PASSWORD = "your password"

# 檢查國際空間站衛星位置是否與我的位置相同 If the ISS is close to my current position 
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 < iss_latitude <= MY_LAT+5 and MY_LONG-5 <iss_longitude <= MY_LONG+5:
        return True

# 檢查是否為晚上了  it is currently dark
def is_night():
    parameters = {
        "lat": MY_LAT ,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # 晚上否？
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    # BONUS: run the code every 60 seconds.
    time.sleep(60)
    
    # Then send me an email to tell me to look up.
    if is_iss_overhead() and is_night():

        with smtplib.SMTP("smtp.gmail.com") as connection :

            connection.starttls()

            connection.login(user=MY_EMAIL,password=PASSWORD)

            # send email
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="address",
                                msg=f"Subject:Look UP!!\n\n The ISS is above you in the sky")

