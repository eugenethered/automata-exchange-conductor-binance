import logging

import requests
from conductor.provider.ExchangeDataProvider import ExchangeDataProvider


class BinanceExchangeDataProvider(ExchangeDataProvider):

    def __init__(self, url):
        self.url = url

    def fetch_exchange_instruments(self) -> list:
        logging.info(f'Requesting data from:[{self.url}]')

        response = requests.get(self.url)
        data = response.json()

        logging.debug(f'Received json data -> {data}')

        return data
