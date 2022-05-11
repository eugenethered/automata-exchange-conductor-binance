import unittest

from binanceconductor.extractor.BinanceDataExtractor import BinanceDataExtractor


class BinanceDataExtractorTestCase(unittest.TestCase):

    def test_should_extract_raw_instrument(self):
        raw_data = {'symbol': 'OTCBTC', 'price': '101.01'}
        data_extractor = BinanceDataExtractor()
        raw_instrument = data_extractor.extract(raw_data)
        self.assertEqual(raw_instrument, 'OTCBTC')


if __name__ == '__main__':
    unittest.main()
