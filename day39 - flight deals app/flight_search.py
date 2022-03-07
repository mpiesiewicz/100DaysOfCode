import requests
from credentials import TEQUILA_TOKEN


class FlightSearcher:

    @staticmethod
    def ask(fly_from='WAW',
            fly_to='PAR',
            date_from="12/03/2022",
            date_to="05/06/2022",
            nights_in_dst_from=2,
            nights_in_dst_to=5):

        endpoint = "https://tequila-api.kiwi.com/v2/search"

        headers = {"apikey": TEQUILA_TOKEN}

        query = {
            'fly_from': fly_from,
            'fly_to': fly_to,
            'date_from': date_from,
            'date_to': date_to,
            'nights_in_dst_from': nights_in_dst_from,
            'nights_in_dst_to': nights_in_dst_to,
            'adults': 2,
            'limit': 1
        }

        response = requests.get(endpoint, headers=headers, params=query)
        response.raise_for_status()
        data = response.json()['data'][0]
        data_formatted = {
            'todaysLowest': data['price'],
            'link': data['deep_link']
        }
        return data_formatted
