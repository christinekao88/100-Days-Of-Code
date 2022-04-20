"""
BS4:Python Library，用於從HTML和XML文件中提取數據

always check http://web root/robots.txt (看網站爬取的限制)
"""

# BeautifulSoup class
from bs4 import BeautifulSoup

with open("100 days\Day_42_Web_scraping_bs4\website.html", encoding='UTF-8') as file:
    contents = file.read()

# 1. 指定用甚麼"markup的內容"來做soup
# 2. 提供解析器 : 幫助理解前面的內容是用甚麼樣的語言結構
soup = BeautifulSoup(contents,'html.parser')
# 取得html內容
print(soup.prettify())

# 取得title tag整串文字
print(soup.title)

# 取得title tag名稱
print(soup.title.name)

# 取得title tag文字內容
print(soup.title.string)

# 用TAG去尋找
# 找到所有 tag = a 的標籤
all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    # 取得tag文字內容
    print(tag.getText())
    # get()可以得到任何一個屬性的值
    print(tag.get("href"))

# 用Attributes去尋找，looking for one
# 找tag =h1 , id= name
heading = soup.find(name="h1",id="name")
print(heading)

# class為python內的保留關鍵字，只能用於創建class
section_heading = soup.find(name="h3",class_="heading")
# 
print(section_heading)
# 取得文字
print(section_heading.getText())
# 取得tag name
print(section_heading.name)
# 取得class value
print(section_heading.get("class"))

# 使用css選擇器"p a"
# select回傳所有匹配的
# select_one回傳第一個匹配的
# 我們要找一個位於p tag裡的a tag
company_url = soup.select_one(selector="p a")
print(company_url)

# select by id
name = soup.select_one("#name")
print(name)

# CSS selector by CLASS 
headings = soup.select(".heading")
print(headings)