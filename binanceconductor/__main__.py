import logging

from cache.holder.RedisCacheHolder import RedisCacheHolder
from cache.provider.RedisCacheProviderWithHash import RedisCacheProviderWithHash
from config.report.holder.ConfigReporterHolder import ConfigReporterHolder
from core.arguments.command_line_arguments import url_option_arg_parser
from logger.ConfigureLogger import ConfigureLogger
from metainfo.MetaInfo import MetaInfo

from binanceconductor.BinanceExchangeConductor import BinanceExchangeConductor


def start():
    ConfigureLogger()

    meta_info = MetaInfo('persuader-technology-automata-exchange-conductor-binance')

    command_line_arg_parser = url_option_arg_parser(meta_info)
    args = command_line_arg_parser.parse_args()

    log = logging.getLogger('Binance Exchange Conductor')
    log.info(f'Binance Exchange Conductor starting with URL {args.url} OPTIONS {args.options}')

    RedisCacheHolder(args.options, held_type=RedisCacheProviderWithHash)

    ConfigReporterHolder(args.options)

    conductor = BinanceExchangeConductor(args.url, args.options)
    conductor.start_process_schedule()


if __name__ == '__main__':
    start()
