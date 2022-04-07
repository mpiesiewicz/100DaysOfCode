import random
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from credentials import chrome_driver_path, INSTAGRAM_LOGIN, INSTAGRAM_PASSWORD, INSTAGRAM_PAGE_TO_FOLLOW


class InstagramBot:
    def __init__(self):
        self.instagram_password = INSTAGRAM_PASSWORD
        self.instagram_login = INSTAGRAM_LOGIN
        self.page_to_follow = INSTAGRAM_PAGE_TO_FOLLOW
        self.chrome_driver_path = chrome_driver_path
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

    def login_to_instagram(self):
        url = 'https://www.instagram.com'
        self.driver.get(url)
        time.sleep(3)

        # xpath list in appearing order
        allow_cookies_xpath = '/html/body/div[4]/div/div/button[2]'
        login_input_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        password_input_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        dont_save_credentials_btn_xpath = '//*[@id="react-root"]/section/main/div/div/div/div/button'
        do_not_notify_btn_xpath = '/html/body/div[5]/div/div/div/div[3]/button[2]'

        allow_cookies_btn = self.driver.find_element(By.XPATH, allow_cookies_xpath)
        allow_cookies_btn.click()
        time.sleep(1)

        login_input = self.driver.find_element(By.XPATH, login_input_xpath)
        login_input.send_keys(self.instagram_login)

        password_input = self.driver.find_element(By.XPATH, password_input_xpath)
        password_input.send_keys(self.instagram_password)
        password_input.send_keys(Keys.ENTER)

        time.sleep(3)
        dont_save_credentials_btn = self.driver.find_element(By.XPATH, dont_save_credentials_btn_xpath)
        dont_save_credentials_btn.click()

        time.sleep(2)
        do_not_notify_btn = self.driver.find_element(By.XPATH, do_not_notify_btn_xpath)
        do_not_notify_btn.click()

    def follow_followers(self, profile_url, follow_setting='follow'):
        self.driver.get(profile_url)
        time.sleep(3)

        followers_xpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div'
        all_followers_selector = 'body > div.RnEpo.Yx5HN > div > div > div > div.isgrP > ul > div > li'
        follow_flag_selector = 'div > div.Pkbci > button > div'
        follow_btn_selector = 'div > div.Pkbci > button'
        scroll_xpath = '/html/body/div[6]/div/div/div/div[2]'
        stop_following_xpath = '/html/body/div[7]/div/div/div/div[3]/button[1]'

        followers_list = self.driver.find_element(By.XPATH, followers_xpath)
        followers_list.click()
        time.sleep(3)

        scr1 = self.driver.find_element(By.XPATH, scroll_xpath)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
        time.sleep(2)

        all_followers = self.driver.find_elements(By.CSS_SELECTOR, all_followers_selector)

        counter = 0
        today_likes = random.randint(26, 47)
        print(today_likes)

        for follower in all_followers:
            if counter >= today_likes:
                break
            try:
                follower_flag = follower.find_element(By.CSS_SELECTOR, follow_flag_selector).text
            except NoSuchElementException:
                pass
            else:
                print(follower_flag)
                time.sleep(1)
                if follow_setting == 'follow':
                    if follower_flag == 'Obserwuj':
                        follow_btn = follower.find_element(By.CSS_SELECTOR, follow_btn_selector)
                        follow_btn.click()
                        counter += 1
                        print(counter)
                        time.sleep(random.uniform(2.3, 3.5))

                else:
                    if follower_flag != 'Obserwuj':
                        follow_btn = follower.find_element(By.CSS_SELECTOR, follow_btn_selector)
                        follow_btn.click()
                        try:
                            confirm_btn = self.driver.find_element(By.XPATH, stop_following_xpath)
                        except NoSuchElementException:
                            pass
                        else:
                            confirm_btn.click()


if __name__ == '__main__':
    bot = InstagramBot()
    bot.login_to_instagram()
    bot.follow_followers(INSTAGRAM_PAGE_TO_FOLLOW)
