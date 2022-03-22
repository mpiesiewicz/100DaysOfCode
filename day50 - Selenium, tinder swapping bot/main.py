import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from credentials import chrome_driver_path, GMAIL_PASS, GMAIL_ADDRESS

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('start-maximized')
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

user_agent = '--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
chrome_options.add_argument(user_agent)

chrome_options.add_argument(r"--user-data-dir=/home/mpiesiewicz/.config/google-chrome") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
chrome_options.add_argument(r'--profile-directory=Profile 1') #e.g. Profile 3

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.tinder.com'
driver.get(url=url)
time.sleep(2)
login_btn = driver.find_element(By.CSS_SELECTOR, '#t-2073920312 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div > header > div > div:nth-child(2) > div.H\(40px\).Px\(28px\) > a')
login_btn.click()

time.sleep(2)

window_main = driver.window_handles[0]

by_google = driver.find_element(By.CSS_SELECTOR, '#t492665908 > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div:nth-child(4) > span > div.Cur\(p\).focus-button-style > div > button')
by_google.click()

time.sleep(3)
window_popup = driver.window_handles[1]

driver.switch_to.window(window_popup)
time.sleep(1)
email_input = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_input.send_keys(GMAIL_ADDRESS)
email_input.send_keys(Keys.ENTER)

# Here is the end of the project as it's not possible to login via facebook or gmail :(