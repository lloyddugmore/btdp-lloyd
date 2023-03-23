import unittest


def multiply_numbers(a, b):
    return a * b


class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(5, 7), 35)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply_numbers(-2, 3), -6)
        self.assertEqual(multiply_numbers(-5, -7), 35)

    def test_multiply_zero(self):
        self.assertEqual(multiply_numbers(0, 10), 0)
        self.assertEqual(multiply_numbers(2, 0), 0)
