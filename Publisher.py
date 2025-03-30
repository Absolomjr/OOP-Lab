class Publisher:
    def __init__(self, name, location, founded_year):
        self.name = name
        self.location = location
        self.founded_year = founded_year
    
    def display_publisher_info(self):
        return f"Publisher: {self.name}, Location: {self.location}, Founded: {self.founded_year}"

class Magazine(Publisher):
    def __init__(self, name, location, founded_year, issue_number=None):
        super().__init__(name, location, founded_year)
        self.issue_number = issue_number
    
    def publish(self):
        if self.issue_number is None:
            print("Error: Cannot publish without an issue number!")
        else:
            print(f"Publishing magazine issue {self.issue_number} from {self.name}.")
    
    def display_magazine_info(self):
        publisher_info = self.display_publisher_info()
        issue_info = f"Issue Number: {self.issue_number}" if self.issue_number else "No issue number assigned."
        return f"{publisher_info}, {issue_info}"

# Creating two magazine objects
mag1 = Magazine("Tech Times", "New York", 1998, 42)
mag2 = Magazine("Science Weekly", "London", 2005)

# Simulating publishing for each
mag1.publish()
mag2.publish()

# Displaying magazine details
print(mag1.display_magazine_info())
print(mag2.display_magazine_info())



