import unittest
from utility import Utility

class Test_replacestring(unittest.TestCase):

    def test_string(self):
        string = "shruti"
        expect = "Hello, Shruti How Are You?"
        result = Utility.replace_string(string)

        self.assertEqual(expect, result)

    def test_string_min3(self):
        string = "as"
        expect = "Hello, As How Are You"
        result = Utility.replace_string(string)
        self.assertEqual(expect, result)