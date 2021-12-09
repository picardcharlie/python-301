# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

import requests
from bs4 import BeautifulSoup

#url = "https://nwdb.info/experience-table/territory-standing/card-choices"

# Open local file of website because it doesn't like requests.
# So I just right click saved it.  Like I do all the NFTs I see on the internet.

file_in = open("nw_db.html", "r")
data_pull = file_in.read()

# Drop off the .text you would normally do with a requests call.
nw_soup = BeautifulSoup(data_pull, features = "html.parser")

# I want to find out the total storage I would get for different standing in a zone.
# Enter a standing level and pull out how many storage upgrades are available by then.
# and total standing XP needed to get there.

# <tr> <td>5</td>
# <td>1,050</td>
# <td>3,000</td>
# <td class="text-center">Standing Gain, Station fee, Gather</td>
# <td class="text-center">Known</td>
# <td>300</td>
# </tr>

# standing, exp needed that rank, total xp, cards available, title, xp gained
stand = nw_soup.find_all("table")

# row of table
table_row = []
for x in stand[0].findAll('tr'):
    table_row.append(x)

# fill a list with lists of every level.
exp_table = []
for x in range(2, len(table_row)):
    exp_table.append(table_row[x].text.split('\n'))

user_input = int(input("Enter the standing to find out the total storage available: "))


# finds the amount of instances of storage in the XP table.
storage_card = 0
for x in range(0, user_input):
    if "Storage" in exp_table[x][3]:
        storage_card += 1

# start with a base of 1000kg and +25kg for each card selected.
total_storage = 1000 + (storage_card * 25)

total_xp = exp_table[user_input][2]

print(f"You have a total of {total_storage}kg available if every storage card is selected.")
print(f"You will need to earn {total_xp}xp to reach that.")