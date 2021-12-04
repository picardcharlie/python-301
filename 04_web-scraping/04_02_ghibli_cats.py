# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.herokuapp.com/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://ghibliapi.herokuapp.com/"
url = "https://ghibliapi.herokuapp.com/species"

cat_page = requests.get(url)
cat_json = cat_page.json()

#print(cat_json[4])

# cats are in position 4 in list.
# cat_json[4]
# open people link ('people') key word and the link is in a list. and print cat name
#cat_json[4]['people'][LIST]['name']

print("The cats of Ghibli")

for cats in cat_json[4]['people']:
#    print(cats)
    temp_name = requests.get(cats).json()
#    print(temp_name['name'])
    temp_movie = requests.get(temp_name['films'][0]).json()
#    print(temp_movie['title'])
    print(f"The cat {temp_name['name']} is in the film {temp_movie['title']}.")
# from people link open the film and print title

