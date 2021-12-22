# Write a script that takes in two numbers from the user and calculates the quotient (division).
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.

try:
    one = int(input("Please enter the first number: "))
    two = int(input("Enter the second number: "))
    print(f"{one} divided by {two} is {one / two}.")

except ValueError:
    print("please enter a digit.")

except ZeroDivisionError:
    print("It's too hard to divide by zero, please use another noumber.")