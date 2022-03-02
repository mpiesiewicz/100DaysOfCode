##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import random
from credentials import *
import smtplib


def send_email(sender_smtp, sender_port, sender_email, sender_pass, recipient, subject, message):

    with smtplib.SMTP(sender_smtp, sender_port) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_pass)

        header = f'To:{recipient}\n' \
                 f'From:{sender_email}\n' \
                 f'Subject:{subject}\n'

        full_message = header + message

        connection.sendmail(from_addr=sender_email, to_addrs=recipient, msg=full_message)


now = dt.datetime.now()
day = now.day
month = now.month

data = pandas.read_csv('birthdays.csv', index_col=None)
birthdays = data[(data['month'] == month) & (data['day'] == day)]
for index, email in birthdays.iterrows():
    letter_number = random.randint(1, 3)
    template_name = f'letter_templates/letter_{letter_number}.txt'
    with open(template_name) as template_file:
        reader = template_file.read()
        message = reader.replace('[NAME]', email.first_name)
        print(message)
        send_email(sender_smtp=SMTP_GMAIL,
                   sender_port=PORT_GMAIL,
                   sender_pass=PASS_GMAIL,
                   sender_email=MAIL_GMAIL,
                   recipient=email.email,
                   subject='Happy Cake Day!',
                   message=message)