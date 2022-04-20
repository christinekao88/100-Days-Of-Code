from selenium import webdriver
from time import sleep

FB_EMAIL = "FB_EMAIL"
FB_PASSWORD = "FB_PASSWORD"

chrome_driver_path = "//Users/kao_oak/Desktop/VtR_Christine Kao/VS Code/100 days/Day_46_Web_scraping_selenium_linkin/chromedriver"

# webdriver將驅動chrome瀏覽器定完成所有的自動化(provide by chrome)
driver = webdriver.Chrome(chrome_driver_path) # 初始化一個新對象

URL ="https://tinder.com/"

# 打開一個新的瀏覽窗口with with URL
driver.get(URL)

driver.maximize_window()

#Allow cookies
sleep(2)
cookies = driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[2]/div/div/div[1]/button')
cookies.click()

sleep(2)
login_button = driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

sleep(2)
fb_login = driver.find_element_by_xpath('//*[@id="c366415127"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

"""
The Facebook login page opens in a new window. 
In order for our selenium code to work on the new window, we have to switch to the window in front.
In Selenium, each window has a identification handle, we can get all the window handles with:
"""
# print(driver.window_handles) # ['CDwindow-23A1366BD91A2730C3C3A3C0CBC14AB8', 'CDwindow-FDF4CF59F5F10E9F2D294912B1B8C4A2']
#Switch to Facebook login window
base_window = driver.window_handles[0]
# New windows that have popped out from the base_window are further down in the sequence
fb_login_window = driver.window_handles[1]

# We can switch our Selenium to target the new facebook login window by:
driver.switch_to.window(fb_login_window)

# You can print the driver.title to verify that it's the facebook login window that is currently target:
# If successful the printed title should be "Facebook" and not "Tinder | Match. Chat. Date."
# print(driver.title)

#Login and hit enter
sleep(2)
fb_email = driver.find_element_by_name("email")
fb_email.send_keys(FB_EMAIL)

sleep(2)
fb_password = driver.find_element_by_id("pass")
fb_password.send_keys(FB_PASSWORD)

sleep(2)
login = driver.find_element_by_id("loginbutton")
login.click()

#Switch back to Tinder window
sleep(2)
driver.switch_to.window(base_window)
# print(driver.title)

#Delay by 5 seconds to allow page to load.
sleep(5)
#Allow location
location_allow = driver.find_element_by_xpath('//*[@id="c366415127"]/div/div/div/div/div[3]/button[1]')
location_allow.click()

#Disallow notifications
sleep(2)
notification_allow = driver.find_element_by_xpath('//*[@id="c366415127"]/div/div/div/div/div[3]/button[2]')
notification_allow.click()

# # 退出整個瀏覽器
# driver.quit()
