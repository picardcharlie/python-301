# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.

import unittest
import math

class TestMath(unittest.TestCase):
    def test_absolute_negative_number(self):
        self.assertEqual(math.fabs(-1), 2)
        return

    def test_squareroot_of_four(self):
        self.assertEqual(math.sqrt(4), 2.0)
        return

if __name__ == "__main__":
    unittest.main()
