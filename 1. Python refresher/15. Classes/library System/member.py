"""
Library Member model
"""

class Member:
    MAX_BOOK_ALLOWED = 3

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.ownedBook = 0
        self.borrowed_list = []

    def borrow_book(self, book):
        if self.ownedBook <= Member.MAX_BOOK_ALLOWED and book.isAvailable:
            self.borrowed_list.append(book)
            self.ownedBook += 1
            book.mark_borrowed()
        else:
            raise Exception


    def return_book(self, book):
        if book in self.borrowed_list:
            book.mark_returned()
            self.borrowed_list.remove(book)
            self.ownedBook -= 1;

    def __str__(self):
        return f"Member: {self.name}\nUser id: {self.member_id}\nCurrently books owned: {[x.title for x in self.borrowed_list]}\nMax Book allowed: {self.ownedBook}/{Member.MAX_BOOK_ALLOWED}"