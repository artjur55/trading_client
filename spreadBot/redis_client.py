import redis

from spreadBot.config import redis_config


class RedisClient:
    def __init__(self):
        self._config = redis_config
        self._r = redis.StrictRedis(host=self._config['REDIS_HOST'],
                                    port=self._config['REDIS_PORT'],
                                    db=self._config['REDIS_DB'],
                                    charset="utf-8",
                                    decode_responses=True)

    def last_updated(self, pair='BTC-USD'):
        return

    def get_history(self, pair='BTC-USD', period=3600, points=1, date=None):
        return

    def update_history(self, l=None):
        return