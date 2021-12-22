# Write a script that generates an exception.
# Handle this exception with a try/except block.
# For example:
#
# list_ = ["hello world!"]
# print(list_[1])
#
# This raises and exception that needs to be handled.

try:
    age = int(input("Enter your age: "))
    print(f"If you were ten years older, you would be {age + 10} years old.")

except:
    print("Please enter a number.")