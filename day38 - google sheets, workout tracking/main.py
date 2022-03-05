import requests
import datetime
from credentials import \
    NUTRITIONIX_TOKEN, \
    NUTRITIONIX_APPID, \
    SHEETY_TOKEN


date = datetime.datetime.today().strftime('%d/%m/%Y')
time = datetime.datetime.now().strftime('%X')

NUTRITIONIX_URL = 'https://trackapi.nutritionix.com'
EXERCISE_ENDPOINT = '/v2/natural/exercise'

header = {
    'x-app-id': NUTRITIONIX_APPID,
    'x-app-key': NUTRITIONIX_TOKEN,
    'x-remote-user-id': '0'
}

body = {
    'query': input('Enter your activity: ')
}
exercise_response = requests.post(url=f"{NUTRITIONIX_URL}{EXERCISE_ENDPOINT}", headers=header, json=body)
exercises = exercise_response.json()['exercises'][0]
print(exercises)

SHEETY_ENDPOINT = 'https://api.sheety.co/5d68b1baa7b33d460a3afb95a8197651/myWorkouts/workouts'

header = {
    'Authorization': f"Bearer {SHEETY_TOKEN}"
}

body = {
    'workout': {
        'date': date,
        'time': time,
        'exercise': exercises['name'],
        'duration': exercises['duration_min'],
        'calories': exercises['nf_calories'],
        'id': 3
    }
}
response = requests.post(url=SHEETY_ENDPOINT, json=body, headers=header)
print(response.text)
