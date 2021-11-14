# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`

class Pokemon:
    def __init__(self, name, primary_type, max_hp, hp, number):
        self.name = name
        self.primary_type = primary_type
        self.max_hp = max_hp
        self.hp = hp
        self.number = number

    def battle(self, other):
        input(f"{self.name} and {other.name} begin to fight!")
        input(f"{self.name} HP: {self.hp}/{self.max_hp}  {other.name} HP: {other.hp}/{other.max_hp}")
        if self.primary_type == "water" and other.primary_type == "fire":
            print(f"{other.name} has fainted, {self.name} wins!")
            other.hp = (other.hp // 2)
        elif self.primary_type == "fire" and other.primary_type == "grass":
            print(f"{other.name} has fainted, {self.name} wins!")
            other.hp = (other.hp // 2)
        elif self.primary_type == "grass" and other.primary_type == "water":
            print(f"{other.name} has fainted, {self.name} wins!")
            other.hp = (other.hp // 2)
        elif self.primary_type == other.primary_type:
            if (self.number / 3) > (other.number / 2):
                print(f"{other.name} has fainted, {self.name} wins!")
            else:
                print(f"{self.name} has fainted, {other.name} wins!")
                # loses half their current HP.  Use // for int division
                self.hp = self.hp // 2
        else:
            print(f"{self.name} has fainted, {other.name} wins!")
            self.hp = self.hp // 2

    def feed(self):
        # Will heal for 1/4 of max HP each time.  Video game tedium, DO IT TWICE.
        self.hp = self.hp + (self.max_hp // 4)
        # Can't heal up for over max.
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name} eats and is healed for {(self.max_hp // 4)} HP.  They have {self.hp}/{self.max_hp} HP now.")

    def __repr__(self):
        return f"Pokemon(name={self.name}, primary_type={self.primary_type}, max_hp={self.max_hp}, hp={self.hp}, number={self.number})"


