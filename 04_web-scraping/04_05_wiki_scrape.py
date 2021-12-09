# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

url = "https://en.wikipedia.org/wiki/Web_scraping"

import requests
from bs4 import BeautifulSoup
import re

wiki_page = requests.get(url)
wiki_soup = BeautifulSoup(wiki_page.text)
#wiki_links = wiki_soup.find(a class_ ='external text')
#print(wiki_links)
link_list = []

#for link in wiki_soup.find_all("a", class_ ="external text"):
#    print(link.get("href"))

wiki_text = wiki_soup.get_text()
wiki_text_io = open("webscrap_text.txt", "w")
wiki_text_io.write(wiki_text)

# Find all numbers in the text.
digits = re.compile("\d")
wiki_numbers = digits.findall(wiki_text)
print(wiki_numbers)

#Really fun reading the RE documentation to do this. REAL FUN.
