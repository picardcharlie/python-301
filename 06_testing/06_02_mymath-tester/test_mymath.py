# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `ZeroDivisionError` gets raised correctly.

import unittest
import mymath

class TestMath(unittest.TestCase):
    def test_check_correct(self):
        self.assertEqual(mymath.subtract_divide(2, 5, 3), 1.0)

    def test_divide_zero(self):
        self.assertEqual(mymath.subtract_divide(2, 5, 5), "This won't work because 5 - 5 = 0.")

