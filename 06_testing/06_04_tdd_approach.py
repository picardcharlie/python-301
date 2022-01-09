# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.


# get user name, age, location

class TestInput(unittest.TestCase):
    def test_number_in_name(self):
        number = None
        for character in script.name:
            if character.isdigit():
                number = True
        self.assertEqual(number, False)

    def test_age_is_numeric(self):
        value = None
        if script.age.isdigit():
            value = True
        self.assertEqual(value, True)

    def test_location_is_local(self):
        self.assertEqual(script.location(state), "Minnesota")