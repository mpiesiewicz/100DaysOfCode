import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from credentials import chrome_driver_path, LINKEDIN_PASS, LINKEDIN_LOGIN

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('start-maximized')
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.linkedin.com'
driver.get(url=url)

email = driver.find_element(By.ID, 'session_key')
password = driver.find_element(By.ID, 'session_password')

email.send_keys(LINKEDIN_LOGIN)
password.send_keys(LINKEDIN_PASS)
password.send_keys(Keys.ENTER)

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=2961145714&f_AL=true&f_E=1%2C2&geoId=105072130&keywords=junior%20python%20developer&location=Polska&sortBy=R&start=25')
timeout = 10

time.sleep(3)

big_box = driver.find_element(By.CSS_SELECTOR, 'body > div.application-outlet > div.authentication-outlet > div.job-search-ext > div.jobs-search-two-pane__wrapper > div > section.jobs-search__left-rail > div > div > ul')
offers = big_box.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
for offer in offers:
    offer.click()
    time.sleep(2)
    save_btn = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
    label = save_btn.find_element(By.CSS_SELECTOR, 'span')
    if label == 'Zapisz':
        time.sleep(2)
        save_btn.click()
        time.sleep(2)

