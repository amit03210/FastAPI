# EXERCISE 1: The Basic Upgrade
# Create a class 'User' with a 'login' method that prints "User logged in".
# Create a child class 'Admin' that inherits from User.
# Add a method 'delete_user' to Admin. 
# Test if an Admin object can both login and delete_user.

from user import User
from admin import Admin

def main():
    ad = Admin('John', 1254)
    us = User('Angel', 545)

    print(ad.login())
    print(ad)
    print(us.login())
    print("Number of user logged:", User.UserOnline)
    print(ad.delete_user())

    print(us)

if __name__ == '__main__':
    main()