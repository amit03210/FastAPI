"""
[ THE STORAGE ]
    Book (Dataclass)  <------- [ ContentValidator (Descriptor) ]
    (Uses __slots__)             (Ensures ISBN/Title isn't empty)
          |
    [ THE ABSTRACTION ]
    BaseMember (ABC)  <------- [ @track_activity (Decorator) ]
    /          \                 (Logs time of every borrow)
   /            \
Librarian      Student (Inheritance)
(Admin)        (User)
   |              |
   +--------------+------> [ BorrowLimit (Descriptor) ]
                                (Enforces max books allowed)

    [ THE ENGINE ]
    LibrarySystem (Orchestrator) <---- [ IStorage (Protocol) ]
    (Main Engine)                      (Handles JSON or Memory)
          |
          | (search_generator: yield)
          v
    [ USER INTERACTION ]
    Search -> Borrow -> Return -> Audit
"""
"""
CAPSTONE PROJECT 2: Cyber-Library Smart Management System

GOAL: Build an automated library system that handles books and members.
This project tests your ability to choose between 'Is-A' (Inheritance) 
and 'Has-A' (Composition).

--- REQUIREMENTS ---

1. DATA LAYER (Dataclasses & Descriptors):
   - Create a 'Book' dataclass. Use '__slots__' for memory efficiency.
   - Implement a 'TitleValidator' descriptor for the Book class. 
     It must ensure the title is a string and not empty.
   - Use a 'BorrowLimit' descriptor on Member classes to ensure 
     Students can't borrow > 3 books and Librarians > 10.

2. SECURITY & LOGGING (Decorators):
   - Create a decorator '@audit_log'. It should print the name of the 
     method being called and the timestamp. 
   - Apply this to 'borrow_book' and 'return_book' methods.

3. ABSTRACTION & CONTRACTS (ABCs & Protocols):
   - Create an ABC 'BaseMember'. 
     - It must have an abstract method 'get_membership_type()'.
     - It must store a list of 'borrowed_books'.
   - Create a Protocol 'IDatabase'.
     - It must define a method 'save(data)' and 'load()'.
     - Create a 'MemoryDB' class that implements this Protocol.

4. SYSTEM LOGIC (Inheritance & Polymorphism):
   - Create 'Student' and 'Librarian' classes inheriting from 'BaseMember'.
   - Librarians should have an extra method 'add_book_to_system()'.
   - Both should implement 'get_membership_type()' differently.

5. THE ENGINE (Composition & Generators):
   - Create 'LibraryEngine'. 
   - COMPOSITION: It should take an 'IDatabase' object in its __init__.
   - CLASS VARIABLE: Track 'total_books_checked_out' globally.
   - GENERATOR: Create 'find_book(author_name)'. It should 'yield' 
     books matching the author to save memory.

--- PROJECT FLOW ---

1. Define the Descriptor 'TitleValidator'.
2. Define the Dataclass 'Book' using the descriptor.
3. Define the Protocol 'IDatabase' and the implementation 'MemoryDB'.
4. Define the ABC 'BaseMember' and subclasses 'Student', 'Librarian'.
5. Build the 'LibraryEngine' to coordinate everything.
6. TEST: Add 5 books, create 1 student, 1 librarian. 
   - Try to over-borrow (trigger Descriptor).
   - Search for books using the generator.
   - Print the global checkout counter.
"""
import datetime
import functools
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Protocol, List, Optional

class TitleValidator:
    
    def __set_name__(self, obj, name):
        self.pub_name = name
    
    def __get__(self, obj, objClass):
        title = obj.__dict__[self.pub_name]
        return title
    
    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise ValueError("Title has to be a string formated")
        elif len(value) == "":
            raise ValueError("Title is empty")
        else:
         obj.__dict__[self.pub_name] = value
         print(f"Setting title of {self.__dict__} to: {value}")

# class TitleValidator:
    
#     def __set_name__(self, obj, name):
#         self.pub_name = name
#         self.private_name = "__" + name
    
#     def __get__(self, obj, objClass):
#         title = getattr(obj, self.private_name)
#         return title
    
#     def __set__(self, obj, value):
#         if not isinstance(value, str):
#             raise ValueError("Title has to be a string formated")
#         elif len(value) == 0:
#             raise ValueError("Title is empty")
#         else:
#          obj.__dict__[self.private_name] = value
#          print(f"Setting title of book to: {value}")

class Book:
    title = TitleValidator()

    def __init__(self, title):
        self.title = title

book1 = Book("Harry Potter")
book2 = Book("Serpant and the water")

print(book1.title)


book1.title = "Cherry in Pot"
print(book1.title)

        
