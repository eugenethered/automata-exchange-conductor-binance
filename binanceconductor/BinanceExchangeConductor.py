import logging

from conductor.ExchangeConductor import ExchangeConductor
from conductor.instrument.InstrumentExchangeHandler import InstrumentExchangeHandler
from conductor.transform.ExchangeTransformer import ExchangeTransformer
from config.report.holder.ConfigReporterHolder import ConfigReporterHolder
from exchangerepo.repository.InstrumentExchangeRepository import InstrumentExchangeRepository
from exchangetransformrepo.repository.ExchangeTransformRepository import ExchangeTransformRepository
from processmanager.ScheduledProcess import ScheduledProcess

from binanceconductor.data.BinanceExchangeDataProvider import BinanceExchangeDataProvider
from binanceconductor.extractor.BinanceDataExtractor import BinanceDataExtractor


class BinanceExchangeConductor(ScheduledProcess):

    def __init__(self, url, options):
        super().__init__(options, 'binance', 'exchange-conductor')
        self.log = logging.getLogger('BinanceExchangeConductor')
        self.url = url
        self.options = options
        self.conductor = self.init_conductor()

    def init_conductor(self):
        transform_repository = ExchangeTransformRepository(self.options)
        data_extractor = BinanceDataExtractor()
        transformer = ExchangeTransformer(self.market, transform_repository, data_extractor)
        data_provider = BinanceExchangeDataProvider(self.url)
        instrument_exchange_repository = InstrumentExchangeRepository(self.options)
        handler = InstrumentExchangeHandler(instrument_exchange_repository)
        return ExchangeConductor(self.options, transformer, data_provider, handler)

    def process_to_run(self):
        self.conductor.get_instrument_exchanges()
        self.log.info('Instrument exchanges data received complete')
        ConfigReporterHolder().delay_missing_storing()
