import requests
from credentials import \
    KEY, \
    TWILLIO_SID, \
    TWILLIO_TOKEN, \
    TWILLIO_PHONE_NUMBER, \
    TO_PHONE_NUMBER_2, \
    TO_PHONE_NUMBER

from datetime import datetime, timezone, timedelta
from twilio.rest import Client

current_hour = datetime.now().hour
WARSAW_LAT = 52.237049
WARSAW_LON = 21.017532

URL = 'https://api.openweathermap.org/data/2.5/onecall'
params = {
    'lat': WARSAW_LAT,
    'lon': WARSAW_LON,
    'appid': KEY,
    'units': 'metric',
    'exclude': 'current,minutely,daily',
}

call = requests.get(url=URL, params=params)
call.raise_for_status()
data = call.json()
print(data)
next_hours = data['hourly'][:13]

will_rain = False
rain_hours = list()

for hour in next_hours:
    weather_id = hour['weather'][0]['id']
    time = datetime.fromtimestamp(hour['dt'], timezone(timedelta(hours=1)))
    if weather_id < 700:
        print(f"Będzie padać o {time.hour}.")  # polish: it's raining at {time.hour}
        rain_hours.append(time.hour)
        will_rain = True
    else:
        print(f"O {time.hour} nie pada.")  # polish: it's not raining at {time.hour}

if will_rain:
    print('Weź parasol')  # polish: take an umbrella
    print(rain_hours)
    client = Client(TWILLIO_SID, TWILLIO_TOKEN)

    # first message
    message = client.messages \
        .create(
            body=f"Weź ☂! Będzie padać o {', '.join(str(x) for x in rain_hours)}",  # pl: it will rain at: rain_hours
            from_=TWILLIO_PHONE_NUMBER,
            to=TO_PHONE_NUMBER,
        )
    print(message.status)

    client = Client(TWILLIO_SID, TWILLIO_TOKEN)

    # second message
    message = client.messages \
        .create(
            body=f"Weź ☂! Będzie padać o {', '.join(str(x) for x in rain_hours)}",  # pl: it will rain at: rain_hours
            from_=TWILLIO_PHONE_NUMBER,
            to=TO_PHONE_NUMBER_2,
        )
    print(message.status)

else:
    print("Dziś nie pada.")  # polish: It won't rain today
