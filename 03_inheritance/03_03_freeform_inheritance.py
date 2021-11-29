# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.


class Game:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs {self.price} dollars."

class DeskTop(Game):
    def __init__(self, name, price, setup_time, players, kids):
        super().__init__(name, price)
        self.setup_time = setup_time
        self.players = players
        self.kids = kids

    def __str__(self):
        return f"{self.name} is a ${self.price} desktop game. It takes {self.setup_type} minutes to setup, has up to {self.players} players and is {self.kids} kid friendly."


class Card(DeskTop):
    def __init__(self, name, price, setup_time, players, kids, deck_type, items):
        super().__init__(name, price, setup_time, players, kids)
        self.deck_type = desk_type
        self.items = items

    def __str__(self):
        return f"{self.name} is a ${self.price} card game. It takes {self.setup_type} minutes to setup, up to {self.players} and is {self.kids} kid friendly. You {self.items} need other items to play and uses a {self.deck_type}."

class Video(Game):
    def __init__(self, name, price, os, type, players, controller):
        super().__init__(name, price)
        self.os = os
        self.type = type
        self.players = players
        self.controller = controller

    def __str__(self):
        return f"{self.name} is a ${self.price} video game.  It runs on {self.os} and {self.controller} use a controller.  It is a {self.players} player {self.type} game."