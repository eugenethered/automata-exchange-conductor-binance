import logging

from conductor.extractor.DataExtractor import DataExtractor
from utility.json_utility import as_data


class BinanceDataExtractor(DataExtractor):

    def extract(self, exchange_instrument_data):
        logging.debug(f'extracting "symbol" from <- {exchange_instrument_data}')
        return as_data(exchange_instrument_data, 'symbol')
