import unittest
from utility import Utility

class Test_Power0f2(unittest.TestCase):

    def test_power_of_2(self):
        n = 2
        expect = [2, 4]
        result = Utility.power_of_2(n)

        self.assertEqual(expect, result)

