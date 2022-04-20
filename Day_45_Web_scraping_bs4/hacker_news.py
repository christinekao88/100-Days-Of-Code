import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/')

yc_web_page = response.text


soup = BeautifulSoup(yc_web_page,'html.parser')

# print(soup.title)

# article_tag = soup.select(".storylink")
# for tag in article_tag:
#     # 取得tag文字內容
#     print(f'Title : {tag.getText()}')
#     # get()可以得到任何一個屬性的值
#     print(f'Link : {tag.get("href")}')

article_tag = soup.find_all(name="a",class_="storylink")
# print(article_tag)

article_texts = []
article_links = []
for article_tag in article_tag:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href") #屬性值
    article_links.append(link)

article_upvotes = [ int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes[0].split()[0])
# print(article_upvotes)

# 找出得分最高的文章
max_point_index = article_upvotes.index(max(article_upvotes))
print(article_texts[max_point_index])
print(article_links[max_point_index])
print(article_upvotes[max_point_index])