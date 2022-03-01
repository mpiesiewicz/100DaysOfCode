import requests
from datetime import datetime
import smtplib
from credentials import *
import time


MY_LAT = 52.229675 # Your latitude
MY_LONG = 21.012230 # Your longitude


def send_email(sender_smtp, sender_port, sender_email, sender_pass, recipient, subject, message):
    with smtplib.SMTP(sender_smtp, sender_port) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_pass)

        header = f'To:{recipient}\n' \
                 f'From:{sender_email}\n' \
                 f'Subject:{subject}\n'

        full_message = header + message
        connection.sendmail(from_addr=sender_email, to_addrs=recipient, msg=full_message)


def is_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_location = iss_response.json()

    iss_latitude = float(iss_location["iss_position"]["latitude"])
    iss_longitude = float(iss_location["iss_position"]["longitude"])
    print(f'lat: {iss_latitude}\n'
          f'long: {iss_longitude}')
    # Your position is within +5 or -5 degrees of the ISS position.
    lat_overhead = MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
    long_overhead = MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    if lat_overhead and long_overhead:
        print(f'is overhead: True')
        return True
    else:
        print(f'is overhead: False')
        return False


# ------- GET SUNSET AND SUNRISE HOURS ------- #

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])+1
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])+1

    # ------------------ DAY CHECK --------------- #
    time_now = datetime.now().hour
    if time_now > sunset or time_now < sunrise:
        print("It's dark!")
        return True
    else:
        print("It's not dark.")
        return False


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
while True:
    if is_overhead():  # and is_dark():
        send_email(sender_smtp=SMTP_GMAIL,
                   sender_port=PORT_GMAIL,
                   sender_email=MAIL_GMAIL,
                   sender_pass=PASS_GMAIL,
                   recipient='michal.piesiewicz@gmail.com',
                   subject='Robobot space notification',
                   message='WARNING - SPACE STATION ABOVE, WATCH YOUR HEAD!')
        print('email sent')
    time.sleep(60)


# BONUS: run the code every 60 seconds.



