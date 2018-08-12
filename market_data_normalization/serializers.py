from rest_framework import serializers
from rest_framework.serializers import Serializer
import arrow

from market_data_normalization.models import MarketNormalizedData, MarketEnum


class BinanceTimestampField(serializers.IntegerField):

    def to_internal_value(self, data):
        extra = 1000  # because binance returns timestamp with microseconds
        return arrow.get(int(data) // extra).datetime


class HitbtcDatetimeIsoField(serializers.DateTimeField):

    def to_internal_value(self, value):
        return arrow.get(value).datetime


class BaseSerializer(Serializer):
    def create(self, validated_data):
        currency_pair = validated_data.pop('currency_pair')
        market = self.get_market()
        from_currency, to_currency = MarketNormalizedData.split_currencies(currency_pair)
        instance = MarketNormalizedData.objects.create(from_currency=from_currency, to_currency=to_currency, market=market, **validated_data)
        return instance


class BinanceSerializer(BaseSerializer):
    s = serializers.CharField(help_text="Currency pair", source="currency_pair")
    h = serializers.CharField(help_text='High price', source="high_price")
    l = serializers.CharField(help_text='Low price', source="low_price")
    o = serializers.CharField(help_text='Last price', source="last_price") # todo: check, is it "o" really last price
    E = BinanceTimestampField(help_text="Bid datetime", source="bid_datetime")

    def get_market(self):
        return MarketEnum.BINANCE


class HitbtcSerializer(BaseSerializer):
    symbol = serializers.CharField(help_text="Currency pair", source="currency_pair")
    high = serializers.CharField(help_text='High price', source="high_price")
    low = serializers.CharField(help_text='Low price', source="low_price")
    last = serializers.CharField(help_text='Last price', source="last_price")
    timestamp = HitbtcDatetimeIsoField(help_text="Bid datetime", source="bid_datetime")

    def get_market(self):
        return MarketEnum.HITBTC




