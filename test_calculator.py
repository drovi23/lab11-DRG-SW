# https://github.com/drovi23/lab11-DRG-SW.git
# Partner 1: Diego Rovigatti Gasparini
# Partner 2: Sam Wolff


import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 3), 4)
        self.assertEqual(add(2, 2), 4)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(2, 2), 0)
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(4, 4), 0)

    # ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(10, 5), 50)
        self.assertEqual(mul(-2, 4), -8)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5.0)
        self.assertAlmostEqual(div(3, 10), 3.33333333)
        self.assertEqual(div(3, -15), -5.0)
        # 3 assertions

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion

        #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    #     fill in code

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(logarithm(2, 2), 1)
        self.assertEqual(logarithm(3, 3), 1)
        self.assertEqual(logarithm(4, 4), 1)

    #     fill in code

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        # Test 3-4-5 triangle
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        # Test 5-12-13 triangle
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        # Test non-integer result
        self.assertAlmostEqual(hypotenuse(1, 1), 1.41421356)

    def test_sqrt(self):  # 3 assertions
        self.assertAlmostEqual(square_root(4), 2.0)
        self.assertAlmostEqual(square_root(25), 5.0)
        self.assertAlmostEqual(square_root(2), 1.41421356)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()