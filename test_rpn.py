import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)

    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)

    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)

    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)

    def test_exponent(self):
        result = rpn.calculate("2 4 ^")
        self.assertEqual(16, result)

    def test_factorial(self):
        result = rpn.calculate("4 !")
        self.assertEqual(24, result)

    def test_int_div(self):
        result = rpn.calculate("8 3 //")
        self.assertEqual(2, result)

    def test_divide_by_0_error(self):
	result = rpn.calculate("5 0 /")
	self.assertEqual("Divide by zero error", result)

if __name__ == '__main__':
    unittest.main()
