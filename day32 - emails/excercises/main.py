import smtplib
from credentials import *
import datetime as dt
import random


def send_email(sender_smtp, sender_port, sender_email, sender_pass, recipient, subject, message):

    with smtplib.SMTP(sender_smtp, sender_port) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_pass)

        header = f'To:{recipient}\n' \
                 f'From:{sender_email}\n' \
                 f'Subject:{subject}\n'

        full_message = header + message

        connection.sendmail(from_addr=sender_email, to_addrs=recipient, msg=full_message)

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
# date_of_birth = dt.datetime(year=1994, month=4, day=13, hour=11)
# print(date_of_birth)


now = dt.datetime.now()
print(now.weekday())
print(now.hour)

with open('quotes.txt') as data_file:
    quotes = data_file.readlines()
    print(len(quotes))
    message = quotes[random.randint(0, len(quotes))]
    print(message)

if now.weekday() == 0 and now.hour == 13:
    send_email(SMTP_GMAIL, PORT_GMAIL, MAIL_GMAIL, PASS_GMAIL, MAIL_YAHOO, 'Quote of the day', message)
    print('message sent')
