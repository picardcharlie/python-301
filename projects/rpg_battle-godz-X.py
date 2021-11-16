# Build a text-based role-playing game that has at least two classes:
# Hero(): the protagonist of your game that the player controls and identifies with. There should be only one hero.
# Opponent(): the challengers that the player meets throughout the gameplay. There should be multiple opponents.
#
# The hero should encounter multiple opponents of different strengths or levels.
# They should be able to perform different actions when meeting an opponent. These actions should be at a minimum:
# attack
# or run away
#
# If the Hero chooses to attack, the program decides through a simulated dice throw that takes the current level
# into account, whether the hero or the opponent wins this round.
# Also implement consequences for winning and losing, e.g. forcing the hero to wait a few seconds before
# continuing the game in case they lose. Or removing the opponent from the opponent pool in case the hero wins.

# try:
# except:
import random

class Hero:
    def __init__(self, name, power, defense, hp, count):
        self.name = name
        self.power = power
        self.defense = defense
        self.hp = hp
        self.count = count

    def battle(self, other):
        # Both start with 3 HP, power needs to break defense, player goes first always, lose 1 per round.
        # Damage can scale with power hitting a large roll.
        # roll 1-20 for attacking.  1 always misses, 20 always hits and +1 damage.
        # Can try to heal, but won't if enemy is able to hit them.
        print(f"You come across a {other.name}, battle!")
        while self.hp > 0:
            choice = int(input("1. Attack  2. Heal  3.Run away.  What do you want to do? "))

            h_roll = random.randint(1, 20)
            o_roll = random.randint(1, 20)
            if choice == 1:
                if h_roll == 20:
                    print("A critical hit!")
                    other.hp -= 2
                elif h_roll == 1:
                    print("A critical miss!")
                elif (h_roll + self.power) > other.defense:
                    print(f"You strike the {other.name}.")
                    other.hp -= 1
                else:
                    print(f"You miss the {other.name}.")

            elif choice == 2:
                if (o_roll + other.power) > self.defense:
                    input(f"The {other.name} stops you and you fail to heal!")
                else:
                    input(f"You avoid the {other.name} and heal yourself some.")
                    self.hp += 1

            elif choice == 3:
                if o_roll == 20:
                    input("You fail to run away.")
                else:
                    input(f"You escape from the {other.name}.")
                    break

            #Enemy turn
            if other.hp <= 0:
                input(f"The {other.name} has been slain.")
                break

            if o_roll == 1:
                print(f"The {other.name} critically misses!")
            elif (o_roll + other.power) > self.defense:
                print(f"The {other.name} hits you.")
                self.hp -= 1
            else:
                print(f"The {other.name} misses you.")

        if self.hp > 0:
            if self.count % 3 == 0:
                self.defense += 1
            else:
                self.power += 1
            self.hp = 3


    def __repr__(self):
        return f"Hero(name={self.name},power={self.power},defense={self.defense},hp={self.hp},count={self.count})"

class Opponent:
    def __init__(self, name, power, defense, hp):
        self.name = name
        self.power = power
        self.defense = defense
        self.hp = hp

    def __repr__(self):
        return f"Opponent(name={self.name},power={self.power},defense{self.defense},hp={self.hp})"

skeleton1 = Opponent("Skeleton", 3, 8, 3)
skeleton2 = Opponent("Skeleton", 3, 8, 3)
skeleton3 = Opponent("Skeleton", 3, 8, 3)
skeleton4 = Opponent("Skeleton", 3, 8, 3)
skeleton5 = Opponent("Skeleton", 3, 8, 3)
bat1 = Opponent("Bat", 1, 5, 3)
bat2 = Opponent("Bat", 1, 5, 3)
slime1 = Opponent("Slime", 3, 17, 3)
slime2 = Opponent("Slime", 3, 17, 3)
ghoul1 = Opponent("Ghoul", 9, 4, 3)
ghoul2 = Opponent("Ghoul", 9, 4, 3)
hobgoblin = Opponent("Hobgoblin", 11, 14, 3)
bluedragon = Opponent("Blue Dragon", 15, 18, 3)

enemy = {1:skeleton1, 2:skeleton2, 3:skeleton3, 4:bat1, 5:bat2, 6:skeleton4, 7:skeleton5, 8:slime1, 9:slime2,
         10:ghoul1, 11:ghoul2, 12:hobgoblin, 13:bluedragon}


print("Welcome to battle godz X!")

# Get hero name, assign stats
name = input("Please enter your name hero: ")
player_power = random.randint(3,10)
player_defense = 13 - player_power
player = Hero(name, player_power, player_defense, 3, 1)

print("You enter the dungeon, looking for a fight...")

directions = ["east", "west", "north", "south", "under", "over", "through"]


while True:

    # if player health is zero, game over.
    if player.hp <= 0:
        input("You have fallen in battle, forgotten in the dark.")
        print("Game Over")
        break

    # check to see if all monsters are dead
    alive = 0
    for x in range(1,14):
        if enemy[x].hp > 0:
            alive = 1

    # if everything has zero hp, you win
    if alive == 0:
        input("You have slain the dungeon, congradulations.")
        print("Game Over")
        break


    # random "movement" to find new monsters
    movement = random.randint(0,6)
    input(f"You move {directions[movement]} to the next room.")

    # check for monster to fight, ignore anything with 0 hp. 13 total.
    monster_fight = 0
    while True:
        mob_num = random.randint(1,13)
        if enemy[mob_num].hp > 0:
            monster_fight = mob_num
            break

    player.battle(enemy[monster_fight])