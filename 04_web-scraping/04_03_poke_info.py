# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

BASE_URL = "https://pokeapi.co/api/v2/"
url = "https://pokeapi.co/api/v2/pokemon/" #{id or name}/

import random
#random.randint(1,150)

import requests
from bs4 import BeautifulSoup

ran_poke = []
for x in range(6):
    ran_poke.append(random.randint(1, 150))

print("These are the best six pokemon in the first generation of pokemon (red/blue).")
for x in ran_poke:
    poke_json = requests.get(url + str(x)).json() # get the page info

#    print(poke_json['types'][0]['type']['name'])

    print(f"{poke_json['name'].capitalize()} is the {x} pokemon and is {poke_json['types'][0]['type']['name']} type.")

# I kinda wanted to do the HTML part, but also no at the same time.
# Thankfully, the link to the guide is down so yeet.