"""
E-Wallet Application Entry Point
"""

from user import User
from wallet import Wallet

def main():
    user1 = User("Alice", 101)
    user2 = User("Bob", 102)

    #perform wallet transaction
    wallet1 = Wallet(user1)
    wallet2 = Wallet(user2)

    wallet1.deposit(1000)
    wallet1.withdraw(200)

    wallet2.deposit(500)

    # Display wallet info
    print(wallet1)

    print("------------------\n")
    
    print(wallet2)
    wallet2.show_transactions()

    # Show total users
    print("\nTotal users created:", User.userCount)

if __name__ == "__main__":
    main()
