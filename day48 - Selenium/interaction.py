from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from credentials import chrome_driver_path

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://en.wikipedia.org/wiki/Main_Page'
driver.get(url=url)

counter = driver.find_element(By.CSS_SELECTOR, '#articlecount > a')
print(counter.text)
# counter.click()

all_portals = driver.find_element(By.LINK_TEXT, 'All portals')
# all_portals.click()

search = driver.find_element(By.NAME, 'search')
search.send_keys('Magda')
search.send_keys(Keys.ENTER)

# driver.quit()
