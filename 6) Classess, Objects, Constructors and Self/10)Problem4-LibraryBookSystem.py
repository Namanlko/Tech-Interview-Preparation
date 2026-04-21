# Problem 4:
"""
Create Book class with:
- Constructor: book_id, title, author, is_issued (default False)
- Methods: issue_book(), return_book(), display_details()
- Class variable to track total books
"""

class Book:

    book_count = 0

    def __init__(self, book_id, title, author, is_issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued=is_issued
        
        Book.book_count += 1

    def issue_book(self):
        if self.is_issued:
            print("Book is Already Issued!")
        else:
            self.is_issued = True
            print("Book Issued Successfully!")

    def return_book(self):
        if not self.is_issued:
            print("Book was not issued!")
        else:
            self.is_issued = False
            print("Book Returned Successfully!")

    def display_details(self):
        print("Book ID:",self.book_id)
        print("Title:",self.title)
        print("Author:",self.author)
        print("Issue Status:","Yes" if self.is_issued else "No")

    @classmethod
    def total_books(cls):
        print("Total Books:", cls.book_count)


b1 = Book(1, "Python Basics", "John Doe")
b2 = Book(2, "OOP Concepts", "Jane Smith")

b1.display_details()
b1.issue_book()
b1.issue_book()   # already issued

b1.return_book()
b1.return_book()  # already returned

Book.total_books()
        