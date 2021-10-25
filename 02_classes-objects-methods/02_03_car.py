# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class CarType:
    """Sets car model, year and max speed"""

    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def faster_faster(self):
        """increases max speed by 5"""
        self.max_speed += 5
        print(f"The {self.year} {self.model} has had its top speed increased to {self.max_speed} speed units!")

    def __str__(self):
        return f"A {self.year} {self.model} with a top speed of {self.max_speed} units."

civic = CarType("Civic", 1997, 95)
focus = CarType("Focus", 2002, 120)

print(civic)
print(focus)

print(civic.faster_faster())
