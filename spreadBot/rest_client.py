from spreadBot.config import auth_config, auth_sandbox
from spreadBot.redis_client import RedisClient

from gdax.authenticated_client import AuthenticatedClient
from gdax.order_book import OrderBook
from gdax.public_client import PublicClient
from gdax.websocket_client import WebsocketClient

from datetime import datetime, time, timedelta


class RestClient:
    def __init__(self):
        self._config = auth_config
        self._sandbox = auth_sandbox
        self._pub = PublicClient()
        self._auth = AuthenticatedClient(self._sandbox['KEY'],
                                         self._sandbox['B64_SECRET'],
                                         self._sandbox['PASSPHRASE'],
                                         api_url=self._sandbox['API_URL'])
        self._redis = RedisClient()

    def pop_history(self, id='BTC-USD', period=300, points=100):
        now = datetime.now()
        delta = timedelta(seconds=period*points)
        start = now-delta
        data = self._pub.get_product_historic_rates(id, start, now, period)
        return data