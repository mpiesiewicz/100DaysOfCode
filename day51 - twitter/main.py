import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from credentials import chrome_driver_path, GMAIL_ADDRESS, GMAIL_PASS

PROMISED_DOWN = 20
PROMISED_UP = 2


class InternetSpeedTwitterBot:
    def __init__(self, promised_down, promised_up):
        self.promised_down = promised_down
        self.promised_up = promised_up
        self.chrome_driver_path = chrome_driver_path
        self.gmail_address = GMAIL_ADDRESS
        self.gmail_pass = GMAIL_PASS
        self.driver = self.initialize_driver()

    @staticmethod
    def initialize_driver():
        chrome_options = Options()
        chrome_options.add_experimental_option('detach', True)
        chrome_options.add_argument('start-maximized')

        user_agent = '--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
        chrome_options.add_argument(user_agent)

        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver

    def get_internet_speed(self):
        url = 'https://www.speedtest.net/pl'
        self.driver.get(url=url)
        time.sleep(5)
        accept_cookies = self.driver.find_element(By.XPATH, '//*[@id="_evidon-banner-acceptbutton"]')
        accept_cookies.click()
        time.sleep(2)
        start = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start.click()
        time.sleep(40)
        download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(f'D: {download_speed}')
        print(f'U: {upload_speed}')
        return download_speed, upload_speed

    def tweet_to_internet_provider(self, download_speed, upload_speed):
        self.driver.execute_script("window.open('https://www.twitter.com')")
        login_google

if __name__ == '__main__':
    bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)
    # download_speed, upload_speed = bot.get_internet_speed()
    bot.tweet_to_internet_provider(20, 7)
