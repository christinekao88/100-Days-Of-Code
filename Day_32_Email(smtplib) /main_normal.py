from datetime import datetime
import pandas as pd
import random
import smtplib


# Create a tuple from today's month and day using datetime. 
today =datetime.now()
today_tuple = (today.month,today.day)
# today = (datetime.now().month, datetime.now().day)

# Use pandas to read the birthdays.csv
data = pd.read_csv("Day_32_Email(smtplib) /birthdays.csv")

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = { (birthday_month, birthday_day): data_row }
# Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
birthdays_dict={(data_row.month,data_row.day): data_row for (index, data_row) in data.iterrows()}

#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    print(birthdays_dict)
    file_path = f"Day_32_Email(smtplib) /letter_templates/letter_{random.randint(1,3)}.txt"
    with open (file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person['name'])
# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.


    my_email = "your email"
    password = "your password"

    with smtplib.SMTP("smtp.gmail.com") as connection :
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person['email'],
                            msg=f"Subject: Happy Birthday\n\n{contents}")



