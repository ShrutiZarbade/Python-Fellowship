import unittest
from utility import Utility


class Test_Harmonicno(unittest.TestCase):

    def test_harmonic(self):
        n = 3
        expect = 1.83
        result = Utility.harmonic_number(n)
        self.assertEqual(expect, round(result, 2))


