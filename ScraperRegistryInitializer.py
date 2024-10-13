from ScraperRegistry import *
from LectureNotesScraper import LectureNotesScraper
from VideoLecturesScraper import VideoLecturesScraper

def initialize_scraper_registry():
    registry = ScraperRegistry()
    registry.register_scraper("Assignments", LectureNotesScraper)
    registry.register_scraper("Lecture Notes", LectureNotesScraper)
    registry.register_scraper("Video Lectures", VideoLecturesScraper)
    registry.register_scraper("Readings", LectureNotesScraper)
    registry.register_scraper("Exams", LectureNotesScraper)
    registry.register_scraper("Recitations", LectureNotesScraper)
    registry.register_scraper("Study Materials", LectureNotesScraper)
    registry.register_scraper("Recitation Videos", VideoLecturesScraper)
    registry.register_scraper("Recitation Notes", LectureNotesScraper)
    registry.register_scraper("Lecture Notes & Slides", LectureNotesScraper)
    registry.register_scraper("Case Studies", LectureNotesScraper)
    registry.register_scraper("Class Videos", VideoLecturesScraper)
    

    return registry