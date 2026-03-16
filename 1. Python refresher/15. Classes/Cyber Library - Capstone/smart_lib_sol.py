import datetime
import functools
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Protocol, List, Optional, Dict

# --- 1. VALIDATION LAYER (Descriptors) ---

class TitleValidator:
    """Ensures title is a non-empty string."""
    def __set_name__(self, owner, name):
        self.internal_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.internal_name, "")

    def __set__(self, obj, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError(f"Invalid title: Must be a non-empty string.")
        setattr(obj, self.internal_name, value)

class BorrowLimit:
    """Enforces max books based on membership type."""
    def __init__(self, max_allowed: int):
        self.max_allowed = max_allowed

    def __set_name__(self, owner, name):
        self.internal_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.internal_name, [])

    def __set__(self, obj, value):
        # Value here is the list of borrowed books
        if len(value) > self.max_allowed:
            raise ValueError(f"Limit Reached: Cannot borrow more than {self.max_allowed} books.")
        setattr(obj, self.internal_name, value)

# --- 2. DATA LAYER (Dataclasses) ---

@dataclass
class Book:
    __slots__ = ['_title', 'author', 'isbn'] # Memory efficiency
    title = TitleValidator() # Linking Descriptor
    author: str
    isbn: str

    def __repr__(self):
        return f"'{self.title}' by {self.author}"

# --- 3. SECURITY & LOGGING (Decorators) ---

def audit_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[AUDIT] {timestamp} | Calling: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# --- 4. ABSTRACTION & CONTRACTS (ABCs & Protocols) ---

class IDatabase(Protocol):
    def save(self, data: List[Book]) -> None: ...
    def load(self) -> List[Book]: ...

class MemoryDB:
    """Implementation of IDatabase Protocol."""
    def __init__(self):
        self._storage = []

    def save(self, data: List[Book]):
        self._storage = data
        print(f"[DB] Saved {len(data)} books to memory.")

    def load(self) -> List[Book]:
        return self._storage

class BaseMember(ABC):
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books: List[Book] = []

    @abstractmethod
    def get_membership_type(self) -> str:
        pass

# --- 5. SYSTEM LOGIC (Inheritance) ---

class Student(BaseMember):
    # Specialized descriptor instance for students
    borrowed_books = BorrowLimit(max_allowed=3)

    def get_membership_type(self) -> str:
        return "Student"

class Librarian(BaseMember):
    # Specialized descriptor instance for librarians
    borrowed_books = BorrowLimit(max_allowed=10)

    def get_membership_type(self) -> str:
        return "Librarian"

    def add_book_to_system(self, engine, book: Book):
        engine.all_books.append(book)
        print(f"[ADMIN] Librarian {self.name} added {book}")

# --- 6. THE ENGINE (Composition & Generators) ---

class LibraryEngine:
    total_checkouts = 0 # Class Variable

    def __init__(self, db: IDatabase):
        self.db = db # Composition
        self.all_books: List[Book] = self.db.load()

    def find_book(self, author_name: str):
        """Generator: Yields books by author."""
        for book in self.all_books:
            if book.author.lower() == author_name.lower():
                yield book

    @audit_log
    def borrow_book(self, member: BaseMember, book_title: str):
        for book in self.all_books:
            if book.title == book_title:
                # This triggers the BorrowLimit descriptor __set__
                new_list = member.borrowed_books + [book]
                member.borrowed_books = new_list 
                
                self.all_books.remove(book)
                LibraryEngine.total_checkouts += 1
                print(f"[SUCCESS] {member.name} borrowed {book_title}")
                return
        print(f"[ERROR] Book {book_title} not found.")

# --- 7. TESTING THE SYSTEM ---

if __name__ == "__main__":
    # Setup
    db = MemoryDB()
    engine = LibraryEngine(db)
    admin = Librarian("Sarah")

    # Add Books
    admin.add_book_to_system(engine, Book("Python Deep Dive", "Luciano Ramalho", "111"))
    admin.add_book_to_system(engine, Book("Clean Code", "Robert Martin", "222"))
    admin.add_book_to_system(engine, Book("The Hobbit", "J.R.R. Tolkien", "333"))
    admin.add_book_to_system(engine, Book("Lord of the Rings", "J.R.R. Tolkien", "444"))

    # Student interaction
    john = Student("John Doe")
    
    # Test Audit Decorator & Borrowing
    engine.borrow_book(john, "Python Deep Dive")
    engine.borrow_book(john, "Clean Code")
    engine.borrow_book(john, "The Hobbit")

    # Test Descriptor (Should raise error - 4th book for Student)
    try:
        print("\n--- Testing Student Borrow Limit (Max 3) ---")
        engine.borrow_book(john, "Lord of the Rings")
    except ValueError as e:
        print(f"Caught expected limit: {e}")

    # Test Generator
    print("\n--- Searching for books by Tolkien ---")
    for book in engine.find_book("J.R.R. Tolkien"):
        print(f"Found: {book}")

    # Final Stats
    print(f"\nTotal System Checkouts: {LibraryEngine.total_checkouts}")