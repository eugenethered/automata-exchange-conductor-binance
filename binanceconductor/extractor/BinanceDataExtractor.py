import logging

from conductor.extractor.DataExtractor import DataExtractor
from coreutility.collection.dictionary_utility import as_data


class BinanceDataExtractor(DataExtractor):

    def __init__(self):
        self.log = logging.getLogger('Binance Exchange Conductor > BinanceDataExtractor')

    def extract(self, exchange_instrument_data):
        self.log.debug(f'extracting "symbol" from <- {exchange_instrument_data}')
        return as_data(exchange_instrument_data, 'symbol')
