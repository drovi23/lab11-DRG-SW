import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(10, 5), 50)
        self.assertEqual(mul(-2, 4), -8)
        self.assertEqual(mul(0, 100), 0)
    def test_divide(self):
        self.assertEqual(div(10, 2), 5.0)
        self.assertAlmostEqual(div(10, 3), 3.33333333)
        self.assertEqual(div(-15, 3), -5.0)
        # 3 assertions


    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
                log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        # Test 3-4-5 triangle
            self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
            # Test 5-12-13 triangle
            self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
            # Test non-integer result
            self.assertAlmostEqual(hypotenuse(1, 1), 1.41421356)

    def test_sqrt(self): # 3 assertions
        self.assertAlmostEqual(square_root(-1))
        self.assertAlmostEqual(square_root(25), 5.0)
        self.assertAlmostEqual(square_root(2), 1.41421356)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()