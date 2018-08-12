import json
from django.test import TestCase

from market_data_normalization.tasks import binance_normalize_task, hitbtc_normalize_task
from market_data_normalization.models import MarketNormalizedData


class BinanceNormalizeTestCase(TestCase):

    def test_binance_normalize_ok(self):

        data_in = {
            "stream": "!miniTicker@arr@1000ms",
            "data": [{
                "e": "24hrMiniTicker",
                "E": 1533573104703,
                "s": "ETHBTC",
                "c": "0.09947500",
                "o": "0.09959600",
                "h": "0.10140000",
                "l": "0.09895200",
                "v": "20967.06500000",
                "q": "2097.13307061"
            }, {
                "e": "24hrMiniTicker",
                "E": 1533573104675,
                "s": "BTCXRP",
                "c": "6956.50000000",
                "o": "7015.33000000",
                "h": "7160.00000000",
                "l": "6861.06000000",
                "v": "32175.20714500",
                "q": "226000493.17069182"
            }]
        }
        binance_normalize_task(data=json.dumps(data_in))
        self.assertEquals(MarketNormalizedData.objects.count(), 2)


class HitbtcNormalizeTestCase(TestCase):

    def test_hitbtc_normalize_ok(self):

        data_in = {
            "jsonrpc": "2.0",
            "method": "ticker",
            "params": {
                "ask": "0.01062",
                "bid": "0.01060",
                "last": "0.01062",
                "open": "0.01059",
                "low": "0.01050",
                "high": "0.01087",
                "volume": "8051.0",
                "volumeQuote": "86.235533",
                "timestamp": "2018-08-06T23:06:16.817Z",
                "symbol": "LTCBTC"
            }
        }
        hitbtc_normalize_task(data=json.dumps(data_in))
        self.assertEquals(MarketNormalizedData.objects.count(), 1)