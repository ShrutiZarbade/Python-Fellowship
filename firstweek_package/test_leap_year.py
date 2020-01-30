import unittest
from utility import Utility

class Test_leap_year(unittest.TestCase):

    def test_leap_year(self):
        a = 2020
        expect = "It is a leap year"
        result = Utility.leap_year(a)
        self.assertEqual(expect, result)

    def test_leap_year_2(self):
        b = 1254
        expect = "It is not a leap year"
        result = Utility.leap_year(b)
        self.assertEqual(expect, result)

    def test_leap_year_3(self):
        c = 14524
        expect = "It's not a 4 digit"
        result = Utility.leap_year(c)
        self.assertEqual(expect, result)

