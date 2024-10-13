import ContentScraperFactory
import Redundant_scripts.LectureVideosScraper as LectureVideosScraper
import VideoLecturesScraper
import DefaultScraper
class ScraperRegistry:
    def __init__(self):
        self._creators = {}

    def register_scraper(self, scraper_type: str, creator):
        """Register a scraper type with its corresponding class"""
        self._creators[scraper_type] = creator

    def create_scraper(self, scraper_type: str) -> ContentScraperFactory:
        """Create and return a scraper instance"""
        creator = self._creators.get(scraper_type)
        if not creator:
            print("Creator not found !!")
            return DefaultScraper.DefaultScraper()
        return creator()  # Call the creator to get an instance