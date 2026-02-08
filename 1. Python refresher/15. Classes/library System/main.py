"""
Library System Entry Point
"""

from book import Book
from member import Member

def main():
    book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "B019PIOJYU")
    member1 = Member("John", 1254)
    member1.borrow_book(book1)

    print(member1)

if __name__ == "__main__":
    main()
