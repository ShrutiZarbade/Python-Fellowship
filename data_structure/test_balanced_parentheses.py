import unittest
from utility_second_week import BalancedParentheses


class TestBalancedParentheses(unittest.TestCase):
    def test_parentheses(self):
        expression = [(8+2)+(2+5)]
        expect = True
        result = BalancedParentheses().balanced_parentheses(expression)
        self.assertEqual(expect, result)

    def test_parentheses1(self):
        expression = "[{}]"
        expect = True
        result = BalancedParentheses().balanced_parentheses(expression)
        self.assertEqual(expect, result)


