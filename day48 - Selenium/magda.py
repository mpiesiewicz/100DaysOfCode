import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchFrameException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from credentials import chrome_driver_path

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.google.com'
driver.get(url=url)

time.sleep(2) # seconds until popup appears

try: # 2 different popups
    frame = driver.find_element(By.XPATH, '//*[@id="cnsw"]/iframe') #<-locating chrome cookies consent frame
    driver.switch_to.frame(frame)
    driver.find_element(By.XPATH, '//*[@id="introAgreeButton"]').click()#<-looking for introAgreeButton button, but seems google has changed its name since and  it only works in old chrome versions.

except NoSuchElementException:
    driver.find_element(By.XPATH, '//*[@id="L2AGLb"]').click() #<- pay attention to new id.


search = driver.find_element(By.NAME, 'q')
phrase = "jaka jest najpiękniejsza dziewczyna na świecie i najlepsza i super gotuje"
for letter in phrase:
    search.send_keys(letter)
    time.sleep(0.1)


driver.get('https://www.facebook.com/magda.ryl')













