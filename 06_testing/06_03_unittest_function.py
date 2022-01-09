# Demonstrate your knowledge of unittest by first creating a function 
# with input parameters and a return value.
# Once you have a function, write at least two tests for the function 
# that use different assertions. The tests should pass.
# Then, include another test that doesn't pass.
#
# NOTE: You can write both the code as well as the tests for it in this file.
# However, feel free to adhere to best practices and separate your tests and
# the functions you are testing into different files.
# Keep in mind that you will run into an error when you'll attempt to import
# this file, because Python modules can't begin with a number.
# You can rename the file to make it work :)

import unittest
age = input("Enter your age: ")
def user_age(age):
    try:
        age2 = int(age)
        return f"You are {age2} years old."
    except ValueError:
        return f"Please enter a numaric value."

class TestInput(unittest.TestCase):
    def test_float_input(self):
        self.assertEqual(user_age(2.0), "You are 2 years old.")

    def test_value_error(self):
        self.assertEqual(user_age("hi"), "Please enter a numaric value.")

if __name__ == "__main__":
    unittest.main()
