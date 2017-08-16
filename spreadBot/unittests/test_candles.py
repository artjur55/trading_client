from unittest import TestCase
from spreadBot.candles import Candles

from spreadBot.unittests import test_data

c = Candles(name='CheeseIt')


class TestCandles(TestCase):
    def test_parse(self):
        print(c.parse(test_data.rest_response))

    def test_plot(self):
        c.plot()

