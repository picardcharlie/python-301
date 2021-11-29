class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."

class Spice(Ingredient):

    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste

    def __str__(self):
        return f"You have {self.amount} {self.name}. It tastes {self.taste}."

    def grind(self):
        print(f"You now have {self.amount} of ground {self.name}.")

    def shake(self):
        print(f"You have shaken up the {self.name}")

    def expire(self):
        if self.name == "salt":
            print(f"Salt never expires!")
        else:
            print(f"Your {self.name} has expired. It's probably still good.")
            self.name = "old " + self.name

class Vegetable(Ingredient):
    def slice(self):
        self.amount = 2 * self.amount
        print(f"You slice the {self.name} in half, you now have {self.amount}.")

    def expire(self):
        print(f"The {self.name} has rotted.")
        self.name = "rotted " + self.name

c = Ingredient("carrots", 3)
s = Spice("salt", 300, "salty")
#p = Spice("pepper", 20)

c.expire()
#p.expire()
s.expire()

si = Ingredient("salt", 45)
si.expire()
print(s)