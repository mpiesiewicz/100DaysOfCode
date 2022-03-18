import csv
import smtplib
from bs4 import BeautifulSoup
import requests
from credentials import \
    PASS_GMAIL, \
    PORT_GMAIL, \
    MAIL_GMAIL, \
    SMTP_GMAIL, \
    RECIPIENT_EMAIL


class Scraper:
    def run(self):
        notify_list = list()

        for product in self.get_products():
            threshold_price = float(product[0])
            product_url = product[1]
            current_price = self.price_check(product_url)
            if current_price <= threshold_price:
                notify_list.append(product)

        if len(notify_list) > 0:
            self.notify(notify_list)

    def price_check(self, product):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.42',
            'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8'
        }
        response = requests.get(url=product, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'lxml')
        print(soup.prettify())
        price_string = soup.select_one(selector='span .a-price-whole').getText()
        return self.price_parse(price_string)

    def notify(self, notify_list):
        subject = 'Price alert from Richard!'
        body = f'' \
               f'Hi,\n' \
               f'the price of those items are really cool today, check this out!\n\n'

        for item in notify_list:
            body += item[1]
            body += '\n\n'

        body += 'Best regards,' \
                'Bot Richard'

        self.send_email(RECIPIENT_EMAIL, subject, body)

    @staticmethod
    def send_email(recipient, subject, body):
        with smtplib.SMTP(SMTP_GMAIL, PORT_GMAIL) as connection:
            connection.starttls()
            connection.login(user=MAIL_GMAIL, password=PASS_GMAIL)

            header = f"To:{recipient}\n" f"From:{MAIL_GMAIL}\n" f"Subject:{subject}\n"

            full_message = header + body
            full_message = full_message.encode('utf-8')
            connection.sendmail(from_addr=MAIL_GMAIL, to_addrs=recipient, msg=full_message)

    @staticmethod
    def get_products():
        with open('data.csv') as data_file:
            data = csv.reader(data_file, delimiter=',')
            return list(data)[1:]

    @staticmethod
    def price_parse(price_string):
        price = price_string.replace(" ", "")
        price = price.replace(',', '')
        return float(price)
