from django.db import models
from rest_framework.exceptions import ValidationError

from market_data_normalization.exceptions import UnknownCurrencyException


class ChoiceEnum(object):

    @classmethod
    def for_choice(cls):
        return [(v, k) for k, v in cls.__dict__.items() if k.isupper()]

    @classmethod
    def values(cls):
        return [v for k, v in cls.__dict__.items() if k.isupper()]

    @classmethod
    def get_name(cls, value):
        for k, v in cls.__dict__.items():
            if v == value and k.isupper():
                return k
        raise ValueError('%s is not defined' % value)


class CoinEnum(ChoiceEnum):
    BITCOIN = 'BTC'
    ETHEREUM = 'ETH'
    RIPPLE = 'XRP'
    LITECOIN = 'LTC'


class MarketEnum(ChoiceEnum):
    BINANCE = 'Binance'
    HITBTC = 'HitBtc'


class MarketNormalizedData(models.Model):

    from_currency = models.CharField(choices=CoinEnum.for_choice(), max_length=255)
    to_currency = models.CharField(choices=CoinEnum.for_choice(), max_length=255)
    high_price = models.DecimalField(max_digits=15, decimal_places=4)
    low_price = models.DecimalField(max_digits=15, decimal_places=4)
    last_price = models.DecimalField(max_digits=15, decimal_places=4)
    bid_datetime = models.DateTimeField()
    market = models.CharField(choices=MarketEnum.for_choice(), max_length=255, null=False)

    @staticmethod
    def split_currencies(currency_pair):
        currency1, currency2 = currency_pair[:3], currency_pair[3:]
        if not currency1 in CoinEnum.values():
            raise UnknownCurrencyException('Unknown currency %s' % currency1)

        if not currency2 in CoinEnum.values():
            raise UnknownCurrencyException('Unknown currency %s' % currency2)
        return currency1, currency2

