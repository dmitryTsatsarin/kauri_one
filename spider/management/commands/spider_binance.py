from django.core.management.base import BaseCommand
import websocket
from market_data_normalization.tasks import binance_normalize_task

import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Spider"

    def handle(self, *args, **options):
        def on_message(ws, message):
            binance_normalize_task.apply_async(kwargs=dict(data=message))
            logger.info(message)

        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("wss://stream.binance.com:9443/stream?streams=!miniTicker@arr@1000ms", on_message=on_message)
        ws.run_forever()
