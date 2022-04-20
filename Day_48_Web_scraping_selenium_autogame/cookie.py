from selenium import webdriver
# from selenium 的webdriver folder裡有一個common的folder
from selenium.webdriver.common.keys import Keys # Keys Class
import time
chrome_driver_path = "100 days\Day_45_Web_scraping_selium\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path) 

URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)

# seconds = int(driver.find_element_by_id("cps").text.split(":")[1])
# print(seconds)

#Get cookie to click on.
cookie = driver.find_element_by_id("cookie")

#Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]
# print(item_ids)

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while True:
    cookie.click()

    #Every 5 seconds:
    if time.time() > timeout:

        #Get all upgrade <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")

        #Convert <b> text into an integer price.
        item_prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        #Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            # print(cookie_upgrades)
            # print(item_prices)
            # print(item_prices[n])
            # print(item_ids[n])
            cookie_upgrades[item_prices[n]] = item_ids[n]

        #Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        #Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            # print(cost, id)
            if cookie_count > cost:
                affordable_upgrades[cost] = id
        print(affordable_upgrades)

        #Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()
                
        #Add another 5 seconds until the next check
        timeout = time.time() + 5

    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break