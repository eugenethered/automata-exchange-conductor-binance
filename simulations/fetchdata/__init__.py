import logging
import time

from cache.holder.RedisCacheHolder import RedisCacheHolder
from config.report.holder.ConfigReporterHolder import ConfigReporterHolder

from binanceconductor.BinanceExchangeConductor import BinanceExchangeConductor

if __name__ == '__main__':

    url = 'https://api.binance.com/api/v3/ticker/price'

    options = {
        'REDIS_SERVER_ADDRESS': '192.168.1.90',
        'REDIS_SERVER_PORT': 6379,
        'MARKET': 'binance',
        'EXCHANGE_TRANSFORMATIONS_KEY': 'binance:exchange:transformations',
        'MISSING_KEY': 'binance:missing',
        'INSTRUMENT_EXCHANGES_KEY': 'binance:exchange:instruments'
    }

    logging.basicConfig(level=logging.DEBUG)

    RedisCacheHolder(options)

    ConfigReporterHolder(options)

    start_time = time.perf_counter()

    conductor = BinanceExchangeConductor(url, options)
    conductor.run()

    end_time = time.perf_counter()
    print(f"Completed in {end_time - start_time:0.4f} seconds")
