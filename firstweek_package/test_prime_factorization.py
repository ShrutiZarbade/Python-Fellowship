import unittest
from utility import Utility

class Test_prime_factorization(unittest.TestCase):
    def test_prime_factorization(self):
        n = 15
        expect = [3, 5]
        result = Utility.prime_factorization(n)
        self.assertEqual(expect, result)


