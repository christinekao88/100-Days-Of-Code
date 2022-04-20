from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "your mail"
ACCOUNT_PASSWORD = "your password"
PHONE = "YOUR PHONE NUMBER"

chrome_driver_path = "/Users/kao_oak/Desktop/VtR_Christine Kao/VS Code/100 days/Day_46_Web_scraping_selium_linkin/chromedriver"

# webdriver將驅動chrome瀏覽器定完成所有的自動化(provide by chrome)
driver = webdriver.Chrome(chrome_driver_path) # 初始化一個新對象

URL ="https://www.linkedin.com/jobs/search/?geoId=106907071&keywords=Python%20Developer&location=台灣%20Taipei%20City%20台北"

# 打開一個新的瀏覽窗口with with URL
driver.get(URL)

sign_in_button = driver.find_element_by_class_name("nav__button-secondary")
sign_in_button.click()

#Wait for the next page to load.
time.sleep(5)

username = driver.find_element_by_id("username")
username.send_keys(ACCOUNT_EMAIL)

password = driver.find_element_by_id("password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)

# login = driver.find_element_by_css_selector(".login__form_action_container  button")
# login.click()

#Locate the apply button
time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

#Submit the application
submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()
# 退出整個瀏覽器
driver.quit()
