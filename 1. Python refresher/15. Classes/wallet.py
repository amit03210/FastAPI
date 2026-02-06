"""
Wallet logic using OOP
"""

class Wallet:
    MIN_BALANCE = 0

    def __init__(self, owner):
        self.owner = owner      #User object
        self.balance = 0        #initialize balance
        self.transaction = []   #list to store transaction history

    def deposit(self, amount):
        if amount<=0:
            raise ValueError("Desposit must be positive")
        
        self.balance += amount
        self.transaction.append(f"Depsoited: {amount}")

    def withdraw(self, amount):
        if amount<=0:
            raise ValueError("Withdrawal must be positive")
        
        if self.balance - amount < Wallet.MIN_BALANCE:
            raise ValueError("Withdrawal amount greater than balance available.")
        
        self.balance -= amount
        self.transaction.append(f"Withdrawal: {amount}")

    def get_balance(self):
        return self.balance

    def show_transactions(self):
       if not self.transaction:
           return "No transaction yet."
       
       for x in self.transaction:
           print(x)

    def __str__(self):
        return (
            f"Wallet Owner: {self.owner.name}\n"
            f"Balance: {self.balance}"
        )
