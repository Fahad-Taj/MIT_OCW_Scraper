class FileReader:
    def __init__(self, filename): # Constructor which expects the filename
        self.filename = filename

    def read_file(self):
        links = [] # List to store the links
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    links.append(line.strip())
                    print(line.strip())
                    
                return links
            
        except FileNotFoundError:
            print("Error: The file '{self.filename}' was not found")
        except IOError:
            print("Error: An I/O error occurred while accessing '{self.filename}'")
            return []
    
