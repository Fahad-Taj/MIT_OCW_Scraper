from abc import ABC, abstractmethod

class ContentScraperFactory(ABC):
    
    @abstractmethod
    def scrape(self, link: str, folder_name: str, named: bool):
        pass