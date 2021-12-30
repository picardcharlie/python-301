# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?

war_peace = open("/home/monster/python/python-301/05_exceptions/books/war_and_peace.txt", "r").read()
crime_punish = open("/home/monster/python/python-301/05_exceptions/books/crime_and_punishment.txt", "r").read()
pride_prejuice = open("/home/monster/python/python-301/05_exceptions/books/pride_and_prejudice.txt", "r").read()

#[:1]

books = [war_peace, crime_punish, pride_prejuice]

for x in books:
    print(f"The first letter is {x[:1]}")

# I don't understand this at all, when would there be an error?