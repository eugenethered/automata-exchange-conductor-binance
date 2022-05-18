import logging

from cache.holder.RedisCacheHolder import RedisCacheHolder
from config.report.holder.ConfigReporterHolder import ConfigReporterHolder
from core.arguments.command_line_arguments import url_option_arg_parser
from logger.ConfigureLogger import ConfigureLogger

from binanceconductor.BinanceExchangeConductor import BinanceExchangeConductor


def main():
    ConfigureLogger()

    command_line_arg_parser = url_option_arg_parser()
    args = command_line_arg_parser.parse_args()

    log = logging.getLogger('Binance Exchange Conductor')
    log.info(f'Binance Exchange Conductor starting with URL {args.url} OPTIONS {args.options}')

    RedisCacheHolder(args.options)

    ConfigReporterHolder(args.options)

    conductor = BinanceExchangeConductor(args.url, args.options)
    conductor.receive_data()


if __name__ == '__main__':
    main()
