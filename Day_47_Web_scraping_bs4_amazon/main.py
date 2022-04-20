import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import datetime as dt

URL = "https://www.amazon.com/-/zh_TW/Pok%C3%A9mon-Mimikyu-%E6%AF%9B%E7%B5%A8%E5%A1%AB%E5%85%85%E5%8B%95%E7%89%A9%E7%8E%A9%E5%85%B7-%E8%8B%B1%E5%90%8B-20-3/dp/B07HHJ42JM/ref=sr_1_111?dchild=1&keywords=pokemon+toys&pd_rd_r=43aa5b9a-b9ea-4710-91b4-86cdd7cc2b7d&pd_rd_w=9mEFS&pd_rd_wg=YjzQM&pf_rd_p=4fa0e97a-13a4-491b-a127-133a554b4da3&pf_rd_r=GXQ6CVWES8W5DSRJCQ6C&qid=1626170121&sr=8-111"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.content, 'lxml')
# print(soup.prettify())
# price = float(soup.select_one("#priceblock_ourprice").getText().split("$")[1])
price = float(soup.find(id="priceblock_ourprice").getText().split("$")[1])
# print(price)
title = soup.find(id="productTitle").getText().strip()
# print(title)

BUY_PRICE = 19
my_email = "your email"
password = "your password"

if price< BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection :

            connection.starttls()

            # 登入
            connection.login(user=my_email,password=password)

            # send email
            connection.sendmail(
                from_addr=my_email,
                to_addrs="address",
                msg=f"Subject:Amazon Price Alert!\n\n {message}\n {url}")
