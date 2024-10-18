from FileReader import FileReader
from SectionExtracter import SectionExtracter
from VideoLecturesScraper import VideoLecturesScraper
from Redundant_scripts.LectureVideosScraper import LectureVideosScraper
from ScraperRegistry import ScraperRegistry
from NotesScraper import NotesScraper
from ScraperRegistryInitializer import initialize_scraper_registry

FILE_NAME = "links.txt"

file_reader = FileReader(FILE_NAME)
links = file_reader.read_file() # 'links' is a list which contains all the links as strings
registry = initialize_scraper_registry()

for link in links:
    # Scrape all of the sections from the given link
    section_extractor = SectionExtracter(link)
    sections = section_extractor.scrape_sections()

    for section in sections:
        print(section['name'] + " " + section['link'] + '\n')
        content_scraper = registry.create_scraper(section['name'])

        content_scraper.scrape(section['link'], section['name'], True)
        

