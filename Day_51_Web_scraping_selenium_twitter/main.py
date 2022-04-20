from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


PROMISE_UP = 150
PROMISE_DOWN = 20
TWITTER_EMAIL = "TWITTER_EMAIL"
TWITTER_PASSWORD = "TWITTER_PASSWORD"
CHROME_DRIVER_PATH = "//Users/kao_oak/Desktop/VtR_Christine Kao/VS Code/100 days/Day_46_Web_scraping_selenium_linkin/chromedriver"
SPEED_URL ="https://www.speedtest.net/result/11818969631"
TWITTER_URL = "https://twitter.com/login"

class InternetSpeedTwitterBot:
    def __init__(self,driver_path) :
        self.driver = webdriver.Chrome(driver_path)
        self.download = 0
        self.upload = 0
    
    # get the internet speed
    def get_internet_speed(self,speed_url):
        self.driver.get(speed_url)

        # Depending on your location, you might need to accept the GDPR pop-up.
        # accept_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        # accept_button.click()

        sleep(3)
        # button = self.driver.find_element_by_css_selector(".start-button a")
        button = self.driver.find_element_by_class_name("start-text")
        button.click()

        sleep(60)
        self.upload = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        # print(self.up.text)
        self.download = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        # print(self.down.text)

        self.driver.quit()

    # tweet at the provider    
    def tweet_at_provider(self,twitter_url):
        self.driver.get(twitter_url)

        #Login and hit enter
        sleep(3)
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)

        sleep(3)
        password = self.driver.find_element_by_name("session[password]")
        password.send_keys(TWITTER_PASSWORD)

        sleep(3)
        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        login.click()

        sleep(5)
        input_tweets = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.download}down/{self.upload}up when I pay for {PROMISE_DOWN}down/{PROMISE_UP}up?"
        
        sleep(3)
        input_tweets.send_keys(tweet)

        sleep(3)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        sleep(2)
        self.driver.quit()  
        
twitter_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
# twitter_bot.get_internet_speed(SPEED_URL)
twitter_bot.tweet_at_provider(TWITTER_URL)

