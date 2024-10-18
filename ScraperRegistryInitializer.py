from ScraperRegistry import *
from NotesScraper import NotesScraper
from VideoLecturesScraper import VideoLecturesScraper

def initialize_scraper_registry():
    registry = ScraperRegistry()
    registry.register_scraper("Assignments", NotesScraper)
    registry.register_scraper("Lecture Notes", NotesScraper)
    registry.register_scraper("Video Lectures", VideoLecturesScraper)
    registry.register_scraper("Readings", NotesScraper)
    registry.register_scraper("Exams", NotesScraper)
    registry.register_scraper("Recitations", NotesScraper)
    registry.register_scraper("Study Materials", NotesScraper)
    registry.register_scraper("Recitation Videos", VideoLecturesScraper)
    registry.register_scraper("Recitation Notes", NotesScraper)
    registry.register_scraper("Lecture Notes & Slides", NotesScraper)
    registry.register_scraper("Case Studies", NotesScraper)
    registry.register_scraper("Class Videos", VideoLecturesScraper)
    registry.register_scraper("Class Session Videos", VideoLecturesScraper)
    registry.register_scraper("Episode", VideoLecturesScraper)

    return registry