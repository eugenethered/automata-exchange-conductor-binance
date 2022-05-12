import logging

from conductor.ExchangeConductor import ExchangeConductor
from conductor.instrument.InstrumentExchangeHandler import InstrumentExchangeHandler
from conductor.transform.ExchangeTransformer import ExchangeTransformer
from config.report.holder.ConfigReporterHolder import ConfigReporterHolder
from core.market.Market import Market
from exchangerepo.repository.InstrumentExchangeRepository import InstrumentExchangeRepository
from exchangetransformrepo.repository.ExchangeTransformRepository import ExchangeTransformRepository

from binanceconductor.data.BinanceExchangeDataProvider import BinanceExchangeDataProvider
from binanceconductor.extractor.BinanceDataExtractor import BinanceDataExtractor


class BinanceExchangeConductor:

    def __init__(self, url, options):
        self.url = url
        self.options = options
        self.conductor = self.init_conductor()

    def init_conductor(self):
        market = Market.parse(self.options['MARKET'])
        transform_repository = ExchangeTransformRepository(self.options)
        data_extractor = BinanceDataExtractor()
        transformer = ExchangeTransformer(market, transform_repository, data_extractor)
        data_provider = BinanceExchangeDataProvider(self.url)
        instrument_exchange_repository = InstrumentExchangeRepository(self.options)
        handler = InstrumentExchangeHandler(instrument_exchange_repository)
        return ExchangeConductor(self.options, transformer, data_provider, handler)

    def receive_data(self):
        self.conductor.get_instrument_exchanges()
        logging.info('Instrument exchanges data received complete')
        ConfigReporterHolder().delay_missing_storing()
