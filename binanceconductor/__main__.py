import logging

from cache.holder.RedisCacheHolder import RedisCacheHolder
from config.report.holder.ConfigReporterHolder import ConfigReporterHolder
from core.arguments.command_line_arguments import url_option_arg_parser

from binanceconductor.BinanceExchangeConductor import BinanceExchangeConductor


def main():
    command_line_arg_parser = url_option_arg_parser()
    args = command_line_arg_parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    logging.info(f'Binance Exchange Conductor starting with URL {args.url} OPTIONS {args.options}')

    RedisCacheHolder(args.options)

    ConfigReporterHolder(args.options)

    conductor = BinanceExchangeConductor(args.url, args.options)
    conductor.receive_data()


if __name__ == '__main__':
    main()
