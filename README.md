# Automata Binance Exchange Conductor

## Packaging
`python3 -m build`

## Prerequisites
```
REDIS_SERVER_ADDRESS
REDIS_SERVER_PORT
MARKET
EXCHANGE_TRANSFORMATIONS_KEY
MISSING_KEY
INSTRUMENT_EXCHANGES_KEY
```

## Deployment

### Deployment Prerequisites
1. `python3 -m pip install --upgrade pip`
2. `pip3 install virtualenv`
3. `python3 -m venv /tmp/automata/conductor/exchange-conductor-binance`

### Deploy Conductor
1. `cd /tmp/automata/conductor/exchange-conductor-binance`
2. `source bin/activate`
3. `pip3 install persuader-technology-automata-exchange-conductor-binance`

### Deploy Clean
1. `deactivate`
2. `rm -fr /tmp/automata/conductor/exchange-conductor-binance` 