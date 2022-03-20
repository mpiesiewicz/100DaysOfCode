from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from credentials import chrome_driver_path

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'http://orteil.dashnet.org/experiments/cookie/'
driver.get(url=url)

cookie = driver.find_element(By.ID, 'cookie')

while True:
    elements = driver.find_elements(By.CSS_SELECTOR, '#store div')
    for element in elements[::-1]:
        try:
            if element.get_attribute('class') == '':
                element.click()
        except StaleElementReferenceException:
            break

    for i in range(400):
        cookie.click()

# driver.quit()
