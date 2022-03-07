from credentials import SHEETY_TOKEN
import requests


class Sheety:
    def __init__(self):
        self.sheety_endpoint = 'https://api.sheety.co/5d68b1baa7b33d460a3afb95a8197651/flightDeals/prices'
        self.header = {
            'Authorization': f"Bearer {SHEETY_TOKEN}"
        }

    def get_destinations(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.header)
        response.raise_for_status()
        print(response.json())
        return response.json()

    def save_results(self, result, row):
        body = {
            'price': result
        }
        endpoint = f"{self.sheety_endpoint}/{row}"
        response = requests.put(url=endpoint, headers={'Authorization': f"Bearer {SHEETY_TOKEN}"}, json=body)
        response.raise_for_status()
        print('saved successfully')
