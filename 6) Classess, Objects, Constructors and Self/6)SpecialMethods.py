# Special Methods - str, repr
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    # String representation (user-friendly)
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    # Official representation (for debugging)
    def __repr__(self):
        return f"{self.title} by {self.author}"

book = Book("Python Basics", "John Doe", 299)

print(book)        # Calls __str__: "Python Basics by John Doe"
print(repr(book))  # Calls __repr__: "Book('Python Basics', 'John Doe', 299)"