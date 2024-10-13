from ContentScraperFactory import *
import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class VideoLecturesScraper(ContentScraperFactory):
    def scrape(self, link: str, folder_name: str, named: bool):
        print("Scraping from VideoLecturesScraper")
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        main_folder_name = self.fetch_main_folder_name(link)
        
        # Create the main folder and transcripts subfolder
        os.makedirs(os.path.join(main_folder_name, folder_name), exist_ok=True)
        
        # Find all lecture links on the homepage
        lecture_divs = soup.find_all('div', class_='video-gallery-card')
        for lecture_div in lecture_divs:
            a_tag = lecture_div.find('a', class_='video-link')
            lecture_url = 'https://ocw.mit.edu' + a_tag['href']
            lecture_name = a_tag.find('h5').text.strip()
            # Scrape and save the transcript
            self.scrape_transcript(lecture_url, lecture_name, main_folder_name)
        # Replace invalid characters in file names
    def sanitize_filename(self, filename):
        return filename.replace(':', '').replace('/', '-').replace('\\', '-').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '').strip()

    def scrape_transcript(self, lecture_url, lecture_name, main_folder_name):
        # Initialize Selenium and open the lecture page
        options = Options()
        options.headless = True  # Run in headless mode to avoid opening the browser window
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        driver.get(lecture_url)
        
        # Wait for the page to load and then click the "Transcript" button
        time.sleep(4)  # Adjust the delay if necessary for slower connections
        
        try:
            transcript_button = driver.find_element(By.XPATH, "//button[contains(@aria-controls, 'transcript')]")
            transcript_button.click()
            time.sleep(1)  # Wait for the transcript section to expand
            
            # Extract the transcript content
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            transcript_div = soup.find('div', class_='transcript-body')
            
            if transcript_div:
                transcript_lines = transcript_div.find_all('div', class_='transcript-line')
                
                # Extract both timestamp and text
                transcript = "\n".join([f"{line.find('span', class_='transcript-timestamp').text} {line.find('span', class_='transcript-text').text}" for line in transcript_lines])

                # Sanitize the lecture name and save the transcript in a text file
                sanitized_lecture_name = self.sanitize_filename(lecture_name)
                filename = os.path.join(main_folder_name, 'transcripts', f'{sanitized_lecture_name}.txt')

                os.makedirs(os.path.dirname(filename), exist_ok=True)  # Create the directory if it doesn't exist
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(transcript)
                print(f'Transcript saved for {lecture_name} at {filename}')
            else:
                print(f'Transcript not found for {lecture_name}')
        
        except Exception as e:
            print(f"Error occurred while scraping transcript: {e}")
        
        finally:
            driver.quit()

    def fetch_main_folder_name(self, homepage_url):
        try:
            homepage_response = requests.get(homepage_url)
            homepage_response.raise_for_status()
            soup = BeautifulSoup(homepage_response.content, 'html.parser')
            # Find the anchor tag that contains the course title
            course_title_tag = soup.find('a', class_="text-capitalize m-0 text-white")
            if course_title_tag:
                return self.sanitize_filename(course_title_tag.text.strip())
            else:
                print("Course title not found, using default folder name.")
                return "Introduction to Algorithms"  # Fallback name
        except requests.exceptions.RequestException as e:
            print(f"Failed to load homepage: {e}")
            return "Error_in_Name"  # Fallback name