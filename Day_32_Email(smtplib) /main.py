##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd 
import random
import smtplib

month = dt.datetime.now().month
day = dt.datetime.now().day

data = pd.read_csv("Day_32_Email(smtplib) /birthdays.csv")
dict = data.to_dict(orient="record")

with open (f"Day_32_Email(smtplib) /letter_templates/letter_{random.randint(1,3)}.txt") as file:
    letter = file.read()
    for record in dict:
        # Check if today matches a birthday in the birthdays.csv
        if month== record['month'] and day== record['day']:
            
            # replace不會改變原文，必須存到新變數才看得到變化
            letter = letter.replace("[NAME]",record['name'])
            my_email = "your email"
            password = "your password"

            with smtplib.SMTP("smtp.gmail.com") as connection :

                connection.starttls()

                # 登入
                connection.login(user=my_email,password=password)

                # send email
                connection.sendmail(from_addr=my_email,
                                    to_addrs=record['email'],
                                    msg=f"Subject: Happy Birthday\n\n{letter}")
