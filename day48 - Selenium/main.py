from credentials import chrome_driver_path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# getting an attribute from amazon - by class
# driver.get(
#     "https://www.amazon.co.uk/Samsung-Galaxy-Mobile-Phone-Smartphone/dp/B08FT71HH5/ref=sr_1_1?keywords=samsung%2Bs20&qid=1638851050&sr=8-1")
#
# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print("Check", price.tag_name)
# print(price.get_attribute('innerHTML'))

# # scraping python.org by name
# driver.get("https://www.python.org")
# search_bar = driver.find_element(By.NAME, 'q')
# print(search_bar.get_attribute('placeholder'))

# scraping by selector
# driver.get("https://www.python.org")
# documentation_link = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')
# print(documentation_link.text)

# scraping by xpath
# driver.get("https://www.python.org")
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# scraping dates
driver.get("https://www.python.org")

results = dict()

items = driver.find_elements(By.CSS_SELECTOR, 'div.medium-widget.event-widget.last > div > ul.menu > li')
for index, item in enumerate(items):
    time = item.find_element(By.CSS_SELECTOR, 'time').text
    name = item.find_element(By.CSS_SELECTOR, 'a').text
    results[index] = {'time': time, 'name': name}

print(results)


driver.quit()

#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li:nth-child(1) > time