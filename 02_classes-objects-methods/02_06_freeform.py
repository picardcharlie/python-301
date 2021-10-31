# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class MeleeWeapon:
    def __init__(self, name, weight, damage_type):
        self.name = name
        self.weight = weight
        self.damage_type = damage_type

    def __str__(self):
        return f"This is a {self.weight}kg {self.name}, it does {self.damage_type} damage."

melee1 = MeleeWeapon("Battle Axe", 12.4, "slash")
melee2 = MeleeWeapon("War Hammer", 17.8, "crush")
print(melee1)
print(melee2)
melee2.weight = 18.5
print(melee2)

class PotionIngredient:
    def __init__(self, name, rarity, use):
        self.name = name
        self.rarity = rarity
        self.use = use

    def __add__(self, other):
        """adds new uses"""
        new_use = self.use + ", " + other.use
        return PotionIngredient(name = self.name, rarity = self.rarity, use = new_use)

    def __str__(self):
        return f"{self.name} is a {self.rarity} ingredient used for {self.use} potions."

pot1 = PotionIngredient("Gromsblood", "rare", "strength")
pot2 = PotionIngredient("Dreamfoil", "common", "mana")
print(pot1)
print(pot2)
pot3 = PotionIngredient("Dreamfoil", "common", "health")
pot4 = pot2 + pot3
print(pot4)

class Familiar:
    def __init__(self, animal, name, magic_type):
        self.animal = animal
        self.name = name
        self.magic_type = magic_type

    def __add__(self, other):
        """Combines magic types"""
        new_animal = self.animal + other.animal
        new_type = self.magic_type + " and " + other.magic_type
        return Familiar(name = self.name, animal = new_animal, magic_type = new_type)

    def __str__(self):
        return f"{self.name} is a {self.animal} that contributes to {self.magic_type} magicks."

fam1 = Familiar("owl", "Cheeze-it", "moon")
fam2 = Familiar("fox", "Dublin", "shadow")
print(fam1)
print(fam2)
fam3 = fam1 + fam2
print(fam3)