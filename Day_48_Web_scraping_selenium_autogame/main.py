# use selenium to interact with browser
# webdriver is bridge between selenium and browser ex:chrome
from selenium import webdriver
chrome_driver_path = "100 days\Day_45_Web_scraping_selium\chromedriver.exe"

# webdriver將驅動chrome瀏覽器定完成所有的自動化(provide by chrome)
driver = webdriver.Chrome(executable_path=chrome_driver_path) # 初始化一個新對象

# URL = "https://www.amazon.com/-/zh_TW/Pok%C3%A9mon-Mimikyu-%E6%AF%9B%E7%B5%A8%E5%A1%AB%E5%85%85%E5%8B%95%E7%89%A9%E7%8E%A9%E5%85%B7-%E8%8B%B1%E5%90%8B-20-3/dp/B07HHJ42JM/ref=sr_1_111?dchild=1&keywords=pokemon+toys&pd_rd_r=43aa5b9a-b9ea-4710-91b4-86cdd7cc2b7d&pd_rd_w=9mEFS&pd_rd_wg=YjzQM&pf_rd_p=4fa0e97a-13a4-491b-a127-133a554b4da3&pf_rd_r=GXQ6CVWES8W5DSRJCQ6C&qid=1626170121&sr=8-111"
URL ="https://www.python.org/"

# 打開一個新的瀏覽窗口with with URL
driver.get(URL)

# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# 當selenium訂為一個特定元素時，以selenium element回傳
search_bar = driver.find_element_by_name("q")
# 向下挖掘各種屬性
# print(search_bar.tag_name) # 得到tag name
# print(search_bar.get_attribute("placeholder")) # 得到屬性placeholder的值

logo = search_bar = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# 指定css class 在之中找a tag
documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

"""
XPath:是一種通過路徑結構來定位特定HTML元素的方法
"""
bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


# event= driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div')
# print(event.text)

event_times = driver.find_elements_by_css_selector(".event-widget time")
# print(type(event_times)) #list
# for time in event_times:
#     print(time.text)

event_names = driver.find_elements_by_css_selector(".event-widget li a")
# for name in event_names:
#     print(name.text)

events={}
for n in range(len(event_times)):
    events[n]={
        "time":event_times[n].text,
        "name":event_names[n].text
    }
print(events)

# 關閉已打開的特定頁面
# driver.close()

# 退出整個瀏覽器
driver.quit()
