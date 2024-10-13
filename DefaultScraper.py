from ContentScraperFactory import *

class DefaultScraper(ContentScraperFactory):
    def scrape(self, link: str, folder_name: str, named: bool):
        print("Printing from default scraper")