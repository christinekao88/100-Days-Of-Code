from selenium import webdriver
# from selenium 的webdriver folder裡有一個common的folder
from selenium.webdriver.common.keys import Keys # Keys Class
chrome_driver_path = "100 days\Day_45_Web_scraping_selium\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path) 

# URL ="https://en.wikipedia.org/wiki/Main_Page"
URL = "http://secure-retreat-92358.herokuapp.com/"
driver.get(URL)

# 只會回傳第一個符合的
# article_count = driver.find_element_by_css_selector("#articlecount a")
# # print(article_count)
# # article_count.click() 

# # 進行文本搜索All portals
# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()

# # 找到search框框
# search = driver.find_element_by_name("search")
# # 並輸入"Python"
# search.send_keys("Python")
# # Keys class 裡有一個常量叫做ENTER
# search.send_keys(Keys.ENTER)

# 找到search框框
fname = driver.find_element_by_name("fName")
# 並輸入"Python"
fname.send_keys("kao")

lname = driver.find_element_by_name("lName")
lname.send_keys("codde")

email = driver.find_element_by_name("email")
email.send_keys("kao@gmail.com")

# 在form內的button
button = driver.find_element_by_css_selector("form button")
button.click()

# 退出整個瀏覽器
# driver.quit()