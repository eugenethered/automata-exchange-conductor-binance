# Automata Binance Exchange Conductor

## Prerequisites
```
REDIS_SERVER_ADDRESS
REDIS_SERVER_PORT
EXCHANGE_TRANSFORMATIONS_KEY
MISSING_KEY
INSTRUMENT_EXCHANGES_KEY
PROCESS_KEY
```

## Docker
* `docker build . -t persuadertechnology/automata-exchange-conductor:binance-0.1 && docker image prune --filter label=stage=BUILDER`

## Publishing to Docker Repository
todo: automate this...
1. `docker push persuadertechnology/automata-exchange-conductor:binance-0.1`

## Publishing Prerequisites
Need to log in to via docker cli i.e. `docker login -u`
