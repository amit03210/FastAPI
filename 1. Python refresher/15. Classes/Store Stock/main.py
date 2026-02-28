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
from product import Product

def main():
   air_conditioner = Product('Samsung', 12000)
   refrigerator = Product.from_csv('Wirlpool,7000')

   print(air_conditioner.price)
   refrigerator.price = 9000
   print(refrigerator.price)
   print(Product.all_products)

if __name__ == '__main__':
   main()