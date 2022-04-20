# SMTP (Simple Mail Transfer Protocol) : 可以連接到電子郵件的一種方式
import smtplib

import datetime as dt
import random

# datetime class
now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()

# create new datetime object
date_of_birth = dt.datetime(year=1998,month=12,day=3)

if weekday==6:    # 0-6 (代表禮拜一到日)
    with open ("Day_32_Email (smtplib) /quotes.txt") as file:
        data = file.readlines()
        send = random.choice(data)


    my_email = "your email"
    password = "your password"

    # create a smtp object from SMTP class -> 放入指定的smtp (hotmail : server smtp.live.com )
    # connection = smtplib.SMTP("smtp.gmail.com")
    with smtplib.SMTP("smtp.gmail.com") as connection :

        # TLS (Transport Layer Security) 代表傳輸層安全，是一種保護與電子郵件服務器連接的方式
        connection.starttls()

        # 登入
        connection.login(user=my_email,password=password)

        # send email
        connection.sendmail(from_addr=my_email,
                            to_addrs="address",
                            msg=f"Subject:Mondy Motivation\n\nTODAY'S Pharse : {send} ")
