from unittest import TestCase

from spreadBot.candles import Candles
from spreadBot.rest_client import RestClient


class TestRestClient(TestCase):
    def test_pop_history(self):
        r = RestClient()
        l = r.pop_history()
        c = Candles(file='100datapoints')
        c.parse(l)
        c.plot()
