# FILE: secure_data.py
"""
SCENARIO: Ensuring user data (like ages or scores) stays within valid ranges.
INSTRUCTIONS:
1. Create a Descriptor class 'RangeValidation'.
   - It should use __set_name__ to store the attribute name.
   - It should use __set__ to check if a value is between 0 and 100.
   - If the value is out of range, raise a ValueError.
2. Create a 'User' class that uses 'RangeValidation' for a 'score' attribute.
3. Test it: Create a user and try setting a score of 150.
4. Awareness Task: Research 'Metaclasses'. Briefly comment on how a 
   Metaclass could automatically add these validators to every class you create.
"""
import logging
logging.basicConfig(level=logging.INFO)

class RangeValidation:
    def __set_name__(self, obj, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, type=None):
        value = getattr(obj, self.private_name)
        logging.info(f"Accessing the {self.public_name}...")
        logging.info(f"The value of \"{self.public_name}\" is {value}")
        return value
   
    def __set__(self, obj, value):
        if value < 0 or value > 100:
            raise ValueError("Out of bound")
        else:
            logging.info(f"Setting value of \"{self.public_name}\" to {value}")
            setattr(obj, self.private_name, value)

   
class User:
    score = RangeValidation()

    def __init__(self, val):
        self.score = val

u1 = User(10)
# u2 = User(101)

print(u1.score)
u1.score = 87
u1.score

#Metaclasses
class ValidationMeta(type):
    def __new__(mcls, name, bases, namespace):
        for attr, validator in namespace.get("__validators__", {}).items():
            if validator == "range":
                namespace[attr] = RangeValidation()
            return super().__new__(mcls, name, bases, namespace)
        
class UserM(metaclass=ValidationMeta):
    __validators__ = {'score': 'range'}

    def __init__(self, score):
        self.score = score

u3 = UserM(30)
print(u3.score)
u3.score = 99
print(u3.score)
# u3.score = 304

# u4 = UserM(139)
            
