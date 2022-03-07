from flight_data import Sheety
from flight_search import FlightSearcher
from notification_manager import NotificationManager
from credentials import SMTP_GMAIL, \
                        PORT_GMAIL, \
                        MAIL_GMAIL, \
                        PASS_GMAIL, \
                        RECIPIENTS


class DataManager:
    def __init__(self):
        self.sheety = Sheety()
        self.flight_searcher = FlightSearcher()
        self.notification_manager = NotificationManager(sender_smtp=SMTP_GMAIL,
                                                        sender_port=PORT_GMAIL,
                                                        sender_address=MAIL_GMAIL,
                                                        password=PASS_GMAIL)
        self.todays_hot_deals = list()

    def run(self):
        self.perform_data_update()
        self.notification_manager.notify(recipients=RECIPIENTS,
                                         content=self.todays_hot_deals)

    def perform_data_update(self):
        destinations = self.get_destinations()
        data_update = self.check_prices(destinations)
        self.save_results(data_update)
        print('Data update done!')

    def save_results(self, data_update):
        for result in data_update:
            if result['todaysLowest'] <= result['lowestPrice']:
                self.sheety.save_results(result, result['id'])
                self.todays_hot_deals.append(result)

    def check_prices(self, destinations):
        data_update = list()
        for destination in destinations['prices']:
            prices_update = self.flight_searcher.ask(fly_to=destination['iataCode'],
                                                     date_from=destination['dateFrom'],
                                                     date_to=destination['dateTo'],
                                                     nights_in_dst_from=destination['minNights'],
                                                     nights_in_dst_to=destination['maxNights'])
            destination.update(prices_update)
            if destination['todaysLowest'] < destination['lowestSoFar']:
                destination['lowestSoFar'] = destination['todaysLowest']
            data_update.append(destination)
        return data_update

    def get_destinations(self):
        return self.sheety.get_destinations()
