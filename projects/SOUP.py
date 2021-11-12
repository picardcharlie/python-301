# For this project, you'll build an ingredient info search script. Your Python code should do the following:
#    Implement the Ingredient() class, where each ingredient has at least a .name and an .amount attribute.
#    Add an instance method called .get_info() that takes the .name attribute of an Ingredient() and creates a Wikipedia URL.
#    The .get_info() method should then automatically open the corresponding Wikipedia page in your web browser

import webbrowser

class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def get_info(self):
        # www.wikipedia.com/wiki/TOPIC
        self.url = "www.wikipedia.com/wiki/" + str(self.name)
        webbrowser.open(self.url, new = 2, autoraise = True)

# test code
# carrot = Ingredient("carrot", 1))
# print(carrot.name)
# carrot.get_info()

while True:
    menu_opt = int(input("Would you like to 1. Enter a new ingredient, 2. Search ingredient: "))
    if menu_opt == 1:
        ing_input = str(input("Enter an ingredient: "))
        ing_amount = input("Enter the amount: ")
        new = Ingredient(ing_input, ing_amount)
    elif menu_opt == 2:
        search_input = input("What ingredient would you like to see: ")
        print(new.name + " " + new.amount)
        new.get_info()
    else:
        break

# While doing this I am wondering how I would impliment this into a database sort of situation.
# How do I keep making new callable objects without overwriting the last one?