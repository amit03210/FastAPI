# Create a custom exception class called 'NotInvitedError'.
# Create a list of guests = ["Alice", "Bob", "Charlie"].
# Ask for a name input. If the name is not in the list, raise NotInvitedError.
# Catch the error and print "Access Denied".
class NotInvitedError(Exception):
    def __init__(self, name):
        self.name = name
    def message(self):
        print(f"Sorry {self.name} is not invited")

name_of_guests = ['Alice', 'Bob', 'Charlie']

try:
    inquiry = input("Please say the name of the guest you want to inquire about.\n")
    if (inquiry not in name_of_guests):
        raise NotInvitedError(inquiry)
    else:
        print("He's invited")
except NotInvitedError as e:
    e.message()