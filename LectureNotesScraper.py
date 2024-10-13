import os
import requests
from ContentScraperFactory import *
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class LectureNotesScraper(ContentScraperFactory):
    def scrape(self, link: str, folder_name: str, named: bool):
        # Step 1: Fetch the webpage content
        response = requests.get(link)
        if response.status_code != 200:
            print(f"Failed to fetch {link}")
            return

        # Step 2: Parse the webpage using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Step 3: Find all <a> tags with '../resources/..' in href
        resource_links = soup.find_all('a', href=lambda x: x and '/resources/' in x)
        
        # Step 4: Find course name from the main page
        course_name_tag = soup.find('a', {'class': 'text-capitalize m-0 text-white'})
        if not course_name_tag:
            print("Course name not found.")
            return
        course_name = course_name_tag.text.strip()

        # Step 5: Create the directory structure
        course_directory = os.path.join(course_name, folder_name)
        os.makedirs(course_directory, exist_ok=True)

        # Step 6: Iterate through the resource links
        for resource_link in resource_links:
            resource_url = urljoin(link, resource_link['href'])
        
            file_name = resource_link.text.strip()
            if(file_name == "PDF"):
                  named = False

            # Step 7: Follow the resource link to get the download page
            resource_response = requests.get(resource_url)
            if resource_response.status_code != 200:
                print(f"Failed to fetch resource page: {resource_url}")
                continue

            # Step 8: Parse the resource page and find the download link
            resource_soup = BeautifulSoup(resource_response.content, 'html.parser')
            download_link_tag = resource_soup.find('a', {'class': 'download-file'})
            if not download_link_tag:
                print(f"No download link found on {resource_url}")
                continue

            download_link = urljoin(resource_url, download_link_tag['href'])

            # Step 9: Download the file
            if(named):
                file_name = ''.join(c for c in file_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
            else:
                file_name = download_link.split('/')[-1]

            file_path = os.path.join(course_directory, file_name)
            print(f"Downloading {file_name}...")

            file_response = requests.get(download_link)
            if file_response.status_code == 200:
                with open(file_path, 'wb') as file:
                    file.write(file_response.content)
                print(f"Downloaded {file_name} to {file_path}")
            else:
                print(f"Failed to download file from {download_link}")

        
        