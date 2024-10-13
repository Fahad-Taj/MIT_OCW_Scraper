import requests
from bs4 import BeautifulSoup

class SectionExtracter:
    def __init__(self, link):
        self.link = link


    def scrape_sections(self):
        sections = []
    
        try:
            # Send a GET request to the page
            response = requests.get(self.link, timeout=10)
            response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
            print("GET request successful")
            
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the <nav> element with class 'course-nav'
            nav = soup.find('nav', class_='course-nav')
            
            if nav:
                # Inside the <nav>, find all <a> tags with class 'text-dark nav-link'
                a_tags = nav.find_all('a', class_='text-dark nav-link')
                
                # Loop through each <a> tag and extract the name and link
                for a in a_tags:
                    link_name = a.get_text(strip=True)  # Extract the visible text of the link
                    link_href = a.get('href', '#')  # Extract the href attribute; default to '#' if missing
                    print(f'Name: {link_name}, Link: {link_href}')
                    
                    # Append the link and name to the links list -------------------------------------
                    sections.append({'name': link_name, 'link': "https://ocw.mit.edu" + link_href})
            else:
                print("Error: <nav> with class 'course-nav' not found.")
        
        except requests.RequestException as e:
            print(f"Error during GET request: {e}")
        
        return sections  # Return the list of links






