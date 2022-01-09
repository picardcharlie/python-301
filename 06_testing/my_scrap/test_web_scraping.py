# testing for my webscrapping script I made.

import unittest
import os
import web_scraping

class TestWebScrap(unittest.TestCase):
# test for connection to website
    def test_website_connection(self):
        url = "https://nwdb.info/experience-table/territory-standing/card-choices"
        page_status = web_scraping.get_page_content(url)
        self.assertEqual(page_status.status_code, 200)

# test if it's protected from scrapping
    def check_for_scrap_protection(self):
        url = "https://nwdb.info/experience-table/territory-standing/card-choices"
        page_data = requests.get(url)
        protected = None
        if "access denied" in page_data:
            protected = True
        self.assertEqual(protected, True)

# test to see if some download wizardry worked if it is protected.
    def test_check_for_downloaded_file(self):
        directory = "/home/monster/python/python-301/06_testing/my_scrap"
        file_found = None
        if "nw_db.html" in os.listdir(directory):
            file_found = True
        self.assertEqual(file_found, True)

# test data can be converted to BeautifulSoup
    def test_for_bs4_object(self):
        soup_object = type(web_scraping.convert_to_bs4(web_scraping.data_pull))
        self.assertEqual(soup_object, "<class 'bs4.BeautifulSoup'>")
# test that the table was built into a list
    def test_table_into_list(self):
        test_table = web_scraping.convert_table(web_scraping.nw_soup)
        table_ok = None
        if len(test_table) == 0 or '\n' in test_table:
            table_ok = False
        self.assertEqual(table_ok, None)

# test to make sure the new list gives accurate data when asked
    def test_table_data(self):
        dataset = web_scraping.convert_table(web_scraping.nw_soup)
        storage, xp = web_scraping.total_storage(dataset, 5)
        self.assertEqual(storage, 1050)
        self.assertEqual(xp, 4275)



if __name__ == "__main__":
    unittest.main()