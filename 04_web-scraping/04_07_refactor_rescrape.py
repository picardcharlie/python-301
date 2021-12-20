# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.

import requests
from bs4 import BeautifulSoup

# data pull function
def DataCall(url):
    if "https:" in url:
        requests_data = requests.get(url)
        soup_data = BeautifulSoup(requests_data, features='html.parser')
    else:
        data = open(url, 'r').read()
        soup_data = BeautifulSoup(data, features='html.parser')
    return soup_data


# clean up data function
def TableClean(data):
    data_table = data.find_all("table")

    # insert rows of table into a list
    table_row = []
    for x in data_table[0].findAll('tr'):
        table_row.append(x)

    # fill a list with lists of every level.
    exp_table = []
    for x in range(2, len(table_row)):
        exp_table.append(table_row[x].text.split('\n'))

    return exp_table

# user input and results
def Storage(table_data):
    user_input = int(input("Enter the standing to find out the total storage available: "))

    storage_card = 0
    for x in range(0, user_input):
        if "Storage" in table_data[x][3]:
            storage_card += 1

    # start with a base of 1000kg and +25kg for each card selected.
    total_storage = 1000 + (storage_card * 25)

    total_xp = table_data[user_input][2]

    print(f"You have a total of {total_storage}kg of extra storage available if every storage card is selected.")
    print(f"You will need to earn {total_xp}xp to reach that.")
    return

Storage(TableClean(DataCall("nw_db.html")))