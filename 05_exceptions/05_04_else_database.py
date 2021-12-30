# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.

# database was so awful y u do dis 2 me?
# Ask for URL, try and get json data from it.  Let's see what error pops up!
# 15s after writing this, it gives A LOT of errors.

import requests

url = input("ENTER URL: ")

try:
    data = requests.get(url)
except requests.exceptions.MissingSchema:
    print("Missing formatting.  Usually 'http://'")
else:
    print(f"{url} returned a {data.status_code} status code and is {data.encoding} encoded.")