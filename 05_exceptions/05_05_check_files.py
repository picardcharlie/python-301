# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = 'integers.txt'

try:
    numbers = open(file_name, "r").read()
    print(type(numbers))

    num_list = []
    for x in numbers.split('\n'):
        num_list.append(int(x))

    for y in num_list:
        print(f"1000 divided by {y} is {1000 // y}")

except ZeroDivisionError:
    print("ERROR: can't divide by zero")

except IOError:
    print("File not found, check folder")