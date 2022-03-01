import requests
from datetime import datetime


# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()
# iss_longitude = data['iss_position']['longitude']
# iss_latitude = data['iss_position']['latitude']
#
# iss_position = (iss_longitude, iss_latitude)
# print(iss_position)
#
# # SUNSET
#
# MY_LAT = 52.229675
# MY_LONG = 21.012230
#
# parameters = {
#     'lat': MY_LAT,
#     'lng': MY_LONG,
#     'formatted': 0,
# }
#
# response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
# response.raise_for_status()
# data = response.json()
# print(data)
# sunrise = data['results']['sunrise']
# sunset = data['results']['sunset']
#
# sunrise = int(sunrise.split('T')[1].split(':')[0])
# sunset = int(sunset.split('T')[1].split(':')[0])
#
# print(f'sunrise: {sunrise}')
# print(f'sunset: {sunset}')
#
#
# print(datetime.now().hour)

time_now = datetime.now().minute
print(time_now)