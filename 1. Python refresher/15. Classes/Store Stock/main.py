# FILE: inventory.py
"""
SCENARIO: Build a system to track store stock.
INSTRUCTIONS:
1. Create 'Product' class with private '__price'.
2. Use @property for 'price' to prevent setting price below 0.
3. Use a Class Variable 'all_products = []' to track every product created.
4. Create a @classmethod 'from_csv(cls, data_string)' that parses "Name,Price" 
   and returns a new Product instance.
"""
