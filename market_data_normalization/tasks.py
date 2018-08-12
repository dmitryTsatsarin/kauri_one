import json

from celery import shared_task

from market_data_normalization.exceptions import UnknownCurrencyException
from .serializers import BinanceSerializer, HitbtcSerializer

import logging
logger = logging.getLogger(__name__)


@shared_task
def binance_normalize_task(data=None):
    try:
        data_dict = json.loads(data)
        for item in data_dict.get('data'):
            serializer = BinanceSerializer(data=item)
            serializer.is_valid(raise_exception=True)
            logger.info(data_dict)
            try:
                serializer.save()
            except UnknownCurrencyException as e:
                logger.error(e)

    except Exception as e:
        logger.error(e)


@shared_task
def hitbtc_normalize_task(data=None):
    try:
        data_dict = json.loads(data)
        params_data =  data_dict.get('params')
        serializer = HitbtcSerializer(data=params_data)
        serializer.is_valid(raise_exception=True)
        logger.info(data_dict)
        try:
            serializer.save()
        except UnknownCurrencyException as e:
            logger.error(e)

    except Exception as e:
        logger.error(e)
