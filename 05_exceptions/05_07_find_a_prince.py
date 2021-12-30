# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".


war_peace = open("/home/monster/python/python-301/05_exceptions/books/war_and_peace.txt", "r").read()
crime_punish = open("/home/monster/python/python-301/05_exceptions/books/crime_and_punishment.txt", "r").read()
pride_prejuice = open("/home/monster/python/python-301/05_exceptions/books/pride_and_prejudice.txt", "r").read()

class PrinceError(Exception):
    def __init__(self, book):
        self.book = book
        self.message = f"A Prince has been found in {self.book}."

try:
    if "Prince" in war_peace[:100]:
        raise PrinceError("War and Peace")

    if "Prince" in crime_punish[:100]:
        raise PrinceError("Crime and Punishment")

    if "Prince" in pride_prejuice[:100]:
        raise PrinceError("Pride and Prejudice")

except PrinceError as pe:
    print(pe.message)


