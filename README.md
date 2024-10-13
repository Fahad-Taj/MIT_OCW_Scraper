
# MIT OCW Readings Scraper

This project is designed to scrape reading materials from MIT OpenCourseWare (OCW) courses and organize them into a structured directory for easy access. The scraper is implemented using Python and utilizes an Abstract Factory pattern to handle scraping functionality for different types of content.

This project uses FactoryPattern, which is a Creational Design pattern in Object Oriented Programming for easier extensibility.

## Features
- **Course-Specific Readings**: Downloads reading materials from specified MIT OCW courses.
- **Customizable Directory Structure**: Each course will have its own directory, and all downloaded files will be stored under a "Readings" folder for that course.
- **Easy to Extend**: The project is designed with an Abstract Factory pattern, making it simple to add support for additional content types.

## Project Structure 
```
.
├── main.py                          
├── <Course name>/
│   ├── Readings/
│   │   ├── [downloaded files]  
```

## Requirements

Install the required dependencies with:
```bash 
pip install -r requirements.txt
```

## Usage
1.  **Clone the repository**:
```bash
git clone https://github.com/your-username/mit-ocw-scraper.git
cd mit-ocw-scraper
```

2. **Insert course links inside the links.txt file**

3. **Run the script**:
```bash
python main.py
```
The reading materials will be downloaded to the respective course's 'section' folder.

## Extending the Scraper
- If you need to scrape other types of content (e.g., videos, assignments), you can extend the ContentScraperFactory and create new scraper classes for each content type. Here's how to add a new type of content scraper:

- Create a new scraper class that inherits from ContentScraperFactory.
- Implement the scrape() method to handle the scraping of the new content type.
- Register the new class in your factory logic to enable dynamic content type creation. Factory logic is implemented inside the ScraperRegistryInitializer.py file

## Project Workflow
This project scrapes reading materials and other sections from MIT OpenCourseWare (OCW) courses and organizes the data into a structured directory format. Here's a step-by-step explanation of how the project works:

- **Course Links Input**: The links.txt file contains a list of URLs for the OCW courses to be scraped. Each link corresponds to a course page on the MIT OCW website.

- **Reading Links from File**: The program reads the links.txt file using the FileReader class and stores all links in a list. These links will be processed in sequence.

```bash
FILE_NAME = "links.txt"
file_reader = FileReader(FILE_NAME)
links = file_reader.read_file()  # 'links' is a list containing course URLs
```

- **Extracting Sections from Course Pages**: For each link in the links list, the SectionExtracter class is used to scrape all section names and section links from the course page. The sections (e.g., "Lecture Notes", "Assignments", etc.) are stored in a dictionary, with each section having a name and a corresponding URL.

```bash
section_extractor = SectionExtracter(link)
sections = section_extractor.scrape_sections()  # Returns a list of sections (name and link)
```

 - **Handling Sections**: Each section is processed by using the ScraperRegistry. This registry checks the section name and constructs the corresponding scraper object. The scraper object knows the structure of the section's webpage and scrapes the relevant content.

```bash
content_scraper = registry.create_scraper(section['name'])
content_scraper.scrape(section['link'], section['name'], True)
```
**Directory Structure**:
Each scraped section is stored inside a folder named after the section (e.g., "Lecture Notes"), which is placed inside a folder named after the course. This ensures that the scraped data is organized and easily accessible.

Example:
For a course named "Physics 101" with sections like "Lecture Notes" and "Assignments", the final directory structure will look like this:

```bash
.
├── Physics 101/
│   ├── Lecture Notes/
│   │   ├── lecture1.pdf
│   │   ├── lecture2.pdf
│   ├── Assignments/
│   │   ├── assignment1.pdf
```
