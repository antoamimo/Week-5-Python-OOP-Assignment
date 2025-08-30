# ASSIGNMENT 1
class Book:
    """
    A class used to represent a physical book.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        publication_year (int): The year the book was published.
        is_available (bool): Indicates if the book is available to check out.
    """

    def __init__(self, title, author, publication_year):
        """
        Initializes the Book object.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            publication_year (int): The year the book was published.
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

    def get_summary(self):
        """
        Returns a summary string with the book's details.
        """
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Published: {self.publication_year}\n"
                f"Status: {'Available' if self.is_available else 'Checked Out'}")

    def check_out(self):
        """
        Changes the book's availability status if it is available.
        """
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        """
        Returns the book, changing its availability status.
        """
        self.is_available = True
        print(f"'{self.title}' has been returned.")


class Ebook(Book):
    """
    A class used to represent an Ebook, inheriting from the Book class.

    Attributes:
        file_size_mb (float): The file size of the ebook in megabytes.
    """

    def __init__(self, title, author, publication_year, file_size_mb):
        """
        Initializes the Ebook object.
        
        Args:
            title (str): The title of the ebook.
            author (str): The author of the ebook.
            publication_year (int): The year the ebook was published.
            file_size_mb (float): The file size of the ebook in MB.
        """
        # Call the parent class's constructor to handle common attributes
        super().__init__(title, author, publication_year)
        self.file_size_mb = file_size_mb

    def get_summary(self):
        """
        Overrides the parent method to include the ebook's unique attribute.
        This demonstrates polymorphism.
        """
        parent_summary = super().get_summary()
        return (f"{parent_summary}\n"
                f"File Size: {self.file_size_mb} MB")
                
# --- Example Usage ---

# Create an instance of the Book class
print("--- Creating a physical book object ---")
physical_book = Book(title="The Begotten", author="Antony Bwana", publication_year=2017)
print(physical_book.get_summary())
print("-" * 20)

# Demonstrate the check_out method
physical_book.check_out()
print("-" * 20)

# Demonstrate the return_book method
physical_book.return_book()
print("-" * 20)

# Create an instance of the Ebook class
print("--- Creating an Ebook object ---")
my_ebook = Ebook(title="MATRIX", author="Andy Weir", publication_year=2011, file_size_mb=2.5)
print(my_ebook.get_summary())
print("-" * 20)

# Note how the check_out method from the parent class still works for the Ebook
my_ebook.check_out()
print(my_ebook.get_summary())

# ASSIGNMENT 2
# This program demonstrates polymorphism using different vehicle classes.

class Car:
    """
    A class representing a car.
    """
    def move(self):
        """
        Defines the move action for a car.
        """
        print("Driving")

class Plane:
    """
    A class representing a plane.
    """
    def move(self):
        """
        Defines the move action for a plane.
        """
        print("Flying")

class Bicycle:
    """
    A class representing a bicycle.
    """
    def move(self):
        """
        Defines the move action for a bicycle.
        """
        print("Riding")

# --- Demonstrating Polymorphism ---

# Create a list of different vehicle objects.
vehicles = [Car(), Plane(), Bicycle()]

print("Let's see how each vehicle moves:")
print("---------------------------------")

# Iterate through the list of vehicles and call the 'move' method on each.
# The same method call (vehicle.move()) results in different outputs
# because of polymorphism.
for vehicle in vehicles:
    vehicle.move()

print("---------------------------------")
print("This shows that while all objects have a 'move' method, each "
      "class implements it differently.")