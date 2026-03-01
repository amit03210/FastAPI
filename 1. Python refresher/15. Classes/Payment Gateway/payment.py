# FILE: payments.py
"""
SCENARIO: Build a system that handles different payment types.
INSTRUCTIONS:
1. Define a Protocol (Interface) called 'PaymentProcessor' with a 'process(amount)' method.
2. Create 'Stripe' and 'PayPal' classes that follow this protocol.
3. Create a function 'checkout(processor: PaymentProcessor, amount)' that 
   doesn't care which class it gets, as long as it has a .process() method.
4. This demonstrates Polymorphism: The behavior changes based on the object passed.
"""
from typing import Protocol

class PaymentProcessor(Protocol):
    def process(self, amount):
        pass

class Stripe:
    def process(self, amount: float) -> None:
        print("Processing amount of ", amount, "via Stipe")
    
class PayPal:
    def process(self, amt: float) -> None:
        print("Amount processed via Paypal")

class RazorPay:
    def process(self, amount: float)-> None:
        print(f"Amount of {amount} has been processed via RazorPay.")


def checkout(processor: PaymentProcessor, amt):
    processor.process(amt)

checkout(Stripe(), 123)
checkout(PayPal(), 111)
checkout(RazorPay(), 2342)