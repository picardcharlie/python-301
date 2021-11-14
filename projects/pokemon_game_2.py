# Then write a second script file that imports your Pokemon() class and write the code for a small battle simulator.
# water, fire, grass

import random
from pokemon_game import Pokemon

poliwag = Pokemon("Poliwag", "water", 40, 40, 1)
krabby = Pokemon("Krabby", "water", 35, 35, 2)
starmie = Pokemon("Starmie", "water", 90, 90, 3)
gyrados = Pokemon("Gyrados", "water", 120, 120, 4)
squirtle = Pokemon("Squirtle", "water", 42, 42, 5)

growlithe = Pokemon("Growlithe", "fire", 40, 40, 6)
ponyta = Pokemon("Ponyta", "fire", 35, 35, 7)
flareon = Pokemon("Flareon", "fire", 90, 90, 8)
moltres = Pokemon("Moltres", "fire", 120, 120, 9)
charmander = Pokemon("Charmander", "fire", 42, 42, 10)

exeggcute = Pokemon("Exeggcute", "grass", 40, 40, 11)
oddish = Pokemon("Oddish", "grass", 35, 35, 12)
tangela = Pokemon("Tangela", "grass", 90, 90, 13)
victreebel = Pokemon("Victreebel", "grass", 120, 120, 14)
bulbasaur = Pokemon("Bulbasaur", "grass", 42, 42, 15)

pdex = {1: poliwag, 2: krabby, 3: starmie, 4: gyrados, 5: squirtle, 6: growlithe, 7: ponyta, 8: flareon, 9: moltres,
           10: charmander, 11: exeggcute, 12: oddish, 13: tangela, 14: victreebel, 15: bulbasaur}

#print(pokedex[2].name)

starter_input = int(input("Please select a starter: 1. Squirtle 2. Charmander 3. Bulbasaur  "))
if starter_input == 1:
    starter = pdex[5]
if starter_input == 2:
    starter = pdex[10]
if starter_input == 3:
    starter = pdex[15]
print(f"You have selected: {starter.name}")

event = 0

while event != 3:
    print(f"{starter.name} HP: {starter.hp}/{starter.max_hp}")
    event = int(input("What would you like to do: 1. Battle 2. Feed 3. Quit  "))
    if event == 1:
        opponent = random.randint(1, 15)
        starter.battle(pdex[opponent])

    if event == 2:
        starter.feed()