# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    def __init__(self):
        self.name = "Uranus"
        self.weight = 8680000000000000000000000
        self.smell = "lavender"
        self.gravity = "low"
        self.weather = "cold"

    def __str__(self):
        return f"{self.name} is a planet that weighs {self.weight}, has {self.gravity} gravity, the weather is {self.weather} and it smells like {self.smell}."

    pass

print(Planet())