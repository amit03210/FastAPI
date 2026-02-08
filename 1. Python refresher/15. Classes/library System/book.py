"""
Book model
"""

class BookException(Exception):
    """Book not Available"""
    def __init__(self, message):
        self().__init__(message)

class Book:
    books = 0   #class attribute

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.isAvailable = True
        self.borrowed = False
        self.returned = False

    def mark_borrowed(self):
        if not self.borrowed:
            self.borrowed = True
            self.returned = False
        else:
            raise BookException("Book not Available")

    def mark_returned(self):
        if self.borrowed:
            self.returned = True
            self.borrowed = False
        else:
            raise BookException("This book is not from here")

    def __str__(self):
        return f"\nTitle: {self.title}\nAuthor: {self.author}\nisbn: {self.isbn}"
