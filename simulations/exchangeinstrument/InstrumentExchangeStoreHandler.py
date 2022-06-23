from cache.holder.RedisCacheHolder import RedisCacheHolder
from cache.provider.RedisCacheProviderWithHash import RedisCacheProviderWithHash
from core.exchange.InstrumentExchange import InstrumentExchange
from exchangerepo.repository.InstrumentExchangeRepository import InstrumentExchangeRepository


class InstrumentExchangeStoreHandler:

    def __init__(self, options):
        self.cache = RedisCacheHolder(options, held_type=RedisCacheProviderWithHash)
        self.instrument_exchange_repository = InstrumentExchangeRepository(options)

    @staticmethod
    def obtain_instrument_exchanges():
        return [
            InstrumentExchange('BTC', 'USDT'),
            InstrumentExchange('BNB', 'USDT')
        ]

    def store_instrument_exchanges(self):
        exchanges = self.obtain_instrument_exchanges()
        print(f'Storing [{len(exchanges)}] instrument exchanges')
        for exchange in exchanges:
            self.instrument_exchange_repository.create(exchange)
        print('Storing complete')
