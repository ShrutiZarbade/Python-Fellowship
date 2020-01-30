import unittest
from utility import Utility


class TestDistance(unittest.TestCase):
    def test_distance(self):
        x = 2
        y = 4
        expect = 4.4721
        result = Utility.distance(x, y)
        self.assertEqual(expect, result)

    def test_distance_2(self):
        x = 0
        y = 1
        expect = 1.0
        result = Utility.distance(x, y)
        self.assertEqual(expect, result)

    def test_distance_3(self):
        x = 5.0
        y = 0.5
        expect = 5.0249
        result = Utility.distance(x, y)
        self.assertEqual(expect, result)






