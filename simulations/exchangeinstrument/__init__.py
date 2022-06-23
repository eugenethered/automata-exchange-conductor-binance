from simulations.exchangeinstrument.InstrumentExchangeStoreHandler import InstrumentExchangeStoreHandler

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '192.168.1.90',
        'REDIS_SERVER_PORT': 6379,
        'INSTRUMENT_EXCHANGES_KEY': 'binance:exchange:mv:instruments'
    }

    store_handler = InstrumentExchangeStoreHandler(options)
    store_handler.store_instrument_exchanges()
