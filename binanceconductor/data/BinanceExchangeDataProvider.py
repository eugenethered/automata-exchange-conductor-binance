import logging

import requests
from conductor.provider.ExchangeDataProvider import ExchangeDataProvider


class BinanceExchangeDataProvider(ExchangeDataProvider):

    def __init__(self, url):
        self.log = logging.getLogger('Binance Exchange Conductor > BinanceExchangeDataProvider')
        self.url = url

    def fetch_exchange_instruments(self) -> list:
        self.log.info(f'Requesting data from:[{self.url}]')

        response = requests.get(self.url)
        data = response.json()

        self.log.debug(f'Received json data -> {data}')

        return data
