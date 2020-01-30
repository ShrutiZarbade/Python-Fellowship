import unittest
from utility import Utility

class Test_anagram(unittest.TestCase):
    def test_anagram(self):
        str1 = "tufbgj"
        str2 = "ufgbjt"
        expect = "It is an anagram"
        result = Utility.anagram(str1, str2)

        self.assertEqual(expect, result)


