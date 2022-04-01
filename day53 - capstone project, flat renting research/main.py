import time

from credentials import chrome_driver_path

import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@dataclass
class Entry:
    title: str
    link: str
    price: str


class ResearchBot:
    def __init__(self):
        self.findings = list()
        self.driver = self.initialize_driver()

    def scrape_olx_data(self):
        url = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/warszawa/'
        params = {
            'search[filter_float_price:from]': 1400,
            'search[filter_float_price:to]': 2000,
            'search[filter_enum_rooms][0]': 'one',
            'search[photos]': 1,
            'search[private_business]': 'private',
            'view': 'list',
            'search[district_id]': 379,
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        print(response.request.url)

        soup = BeautifulSoup(response.text, 'html.parser')
        deals = soup.find_all('div', class_='offer-wrapper')
        for deal in deals:
            name_box = deal.find(name='div', class_='space rel')
            link = name_box.h3.a.get('href')
            title = name_box.h3.a.strong.text
            price = deal.find(name='p', class_='price').text.strip()
            entry = Entry(title, link, price)
            self.findings.append(entry)

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

    def enter_data(self):
        self.driver.get('https://forms.gle/2VqUoGRhBuVxtpxo6')
        time.sleep(2)

        for finding in self.findings:
            inputs = self.driver.find_elements(By.CLASS_NAME, 'whsOnd')
            inputs[0].send_keys(finding.title)
            inputs[1].send_keys(finding.price)
            inputs[2].send_keys(finding.link)
            submit_btn = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            submit_btn.click()
            time.sleep(1)
            send_another_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            send_another_btn.click()
            time.sleep(1)


bot = ResearchBot()
bot.scrape_olx_data()
# bot.findings = [
#     Entry('testowy tytuł 1', 'www.test.pl', '1700'),
#     Entry('testowy tytuł 2', 'www.testowo.pl', '1666'),
# ]
bot.enter_data()
