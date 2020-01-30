import unittest

from utility import Utility

class Test_windchill(unittest.TestCase):
    def test_windchill(self):
        t = 51
        v = 120
        expect = "values are not in range"
        result = Utility.wind_chill(t, v)
        self.assertEqual(expect, result)

    def test_windchill_1(self):
        t = 34
        v = 54
        expect = 16.708
        result = Utility.wind_chill(t, v)
        self.assertEqual(expect, result)

