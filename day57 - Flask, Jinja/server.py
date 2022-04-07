import requests
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    current_year = datetime.now().year
    return render_template('index.html', current_year=current_year)


@app.route('/guess/<name>')
def guess(name):

    def api_call(endpoint, key_to_get):
        params = {'name': name}
        response = requests.get(endpoint, params)
        response.raise_for_status()
        return response.json()[key_to_get]

    age = api_call('https://api.agify.io', 'age')
    gender = api_call('https://api.genderize.io', 'gender')
    nationality = api_call('https://api.nationalize.io', 'country')[0]['country_id']

    return render_template('guess.html', name=name, gender=gender, age=age, nationality=nationality)


if __name__ == '__main__':
    app.run(debug=True)
