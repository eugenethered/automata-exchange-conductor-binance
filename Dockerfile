FROM python:3.10.6-alpine AS BUILDER
LABEL stage=BUILDER
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10.6-alpine
RUN addgroup apprunner && adduser apprunner -D -H -G apprunner
USER apprunner
WORKDIR /app
COPY --from=BUILDER /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --chown=apprunner:apprunner ./binanceconductor ./binanceconductor

ENV PYTHONPATH="${PYTHONPATH}:/app/binanceconductor" \
    REDIS_SERVER_ADDRESS=127.0.0.1 \
    REDIS_SERVER_PORT=6379 \
    EXCHANGE_TRANSFORMATIONS_KEY=binance:transformation:mv:exchange \
    MISSING_KEY=binance:mv:missing \
    INSTRUMENT_EXCHANGES_KEY=binance:exchange:mv:instruments \
    VERSION=0.1 \
    PROCESS_RUN_PROFILE_KEY=binance:process:mv:run-profile \
    PROCESS_KEY=binance:process:mv:status

CMD ["python", "binanceconductor/__main__.py"]
