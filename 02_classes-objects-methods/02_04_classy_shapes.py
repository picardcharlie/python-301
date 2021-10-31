# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.


class Rectangle:
    """Accepts the length and width and calculates the are and parimeter length"""

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = 0
        self.parimeter = 0

    def find_area(self):
        self.area = (self.length * self.width)
        return self.area

    def find_parimeter(self):
        self.parimeter = (self.length * 2) + (self.width * 2)
        return self.parimeter

rec = Rectangle(5, 2)
print(rec.find_area())
print(rec.find_parimeter())

class Circle:
    """accepts the radius of a circle and finds area and circumfrance."""

    def __init__(self, radius):
        self.radius = radius
        self.area = 0
        self.circumference = 0

    def find_area(self):
        self.area = 3.1415 * (self.radius ** 2)
        return self.area

    def find_circumference(self):
        self.circumference = 3.1415 * (self.radius * 2)
        return self.circumference

cir = Circle(8)
print(cir.find_area())
print(cir.find_circumference())