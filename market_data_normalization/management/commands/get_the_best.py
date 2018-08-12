import arrow
from django.core.management.base import BaseCommand
from django.db.models import Q

from market_data_normalization.models import MarketNormalizedData, MarketEnum, CoinEnum


class Command(BaseCommand):
    help = "Get the best"

    def handle(self, *args, **options):
        end = arrow.utcnow()
        timedelta_range = (end.shift(days=-1).datetime, end.datetime) # time interval
        q = Q(bid_datetime__range=timedelta_range, from_currency=CoinEnum.LITECOIN, to_currency=CoinEnum.BITCOIN)

        q_market = Q(market=MarketEnum.BINANCE)
        binance_lowest = MarketNormalizedData.objects.filter(q & q_market).order_by('low_price').first()
        print('The lowest price is %s (for LTCBTC at binance)' % (binance_lowest.low_price if binance_lowest else 0))

        q_market = Q(market=MarketEnum.HITBTC)
        hitbtc_lowest = MarketNormalizedData.objects.filter(q & q_market).order_by('low_price').first()
        print('The lowest price is %s (for LTCBTC at HitBtc)' % hitbtc_lowest.low_price if hitbtc_lowest else 0)
