#!/usr/bin/env bash
sleep 5 && python ./manage.py migrate; # temporary line
python ./manage.py spider_binance &
python ./manage.py spider_hitbtc &
celery worker -A kauri_one -Q market_data_normalization -c 1 --loglevel=info
