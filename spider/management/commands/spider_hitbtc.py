import logging
import queue
import time

from django.core.management.base import BaseCommand
from hitbtc import HitBTC

from market_data_normalization.tasks import hitbtc_normalize_task

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Spider"

    def handle(self, *args, **options):

        # ---------------- example from documentation. Optimize this code
        c = HitBTC(raw=True)
        c.start()  # start the websocket connection
        time.sleep(2)  # Give the socket some time to connect
        r = c.subscribe_ticker(symbol='ETHBTC')  # Subscribe to ticker data for the pair ETHBTC
        c.subscribe_ticker(symbol='LTCBTC')  # Subscribe to ticker data for the pair LTCBTC

        while True:
            try:
                data = c.recv()
            except queue.Empty:
                continue
            # ---------------- END example from documentation
            logger.info(data)
            hitbtc_normalize_task.apply_async(kwargs=dict(data=data))





