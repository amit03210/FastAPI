"""
SCENARIO: Build a system to track store stock.
INSTRUCTIONS:
1. Create 'Product' class with private '__price'.
2. Use @property for 'price' to prevent setting price below 0.
3. Use a Class Variable 'all_products = []' to track every product created.
4. Create a @classmethod 'from_csv(cls, data_string)' that parses "Name,Price" 
   and returns a new Product instance.
"""

class Product:

    all_products = []

    def __init__(self, name, price):
        self.name = name
        self.__price = price
        Product.all_products.append(self)

    @property
    def price(self):
        print(f"Getting price of {self.name}...")
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be less than 0")
        else:
            print(f"Setting price of {self.name}...")
            self.__price = value

    @classmethod
    def from_csv(cls, data_string):
        name, price = data_string.split(',')
        prod = cls(name, float(price))
        return prod
    
    def __repr__(self):
        return f"{self.name} - {self.price}"
    
        

        