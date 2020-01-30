import unittest
from utility_second_week import  Palindrome


class PalindromeTestCase(unittest.TestCase):
    def test_palindrome(self):
        a = "mnnm"
        expect = True
        result = Palindrome().palindrome(a)
        self.assertEqual(expect, result)

    def test_palindrome_checker(self):
        string = "bnbhg"
        expect = False
        result = Palindrome().palindrome(string)
        self.assertEqual(expect, result)
