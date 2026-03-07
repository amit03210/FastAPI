# def smart_wrapper(func):
#     def wrapper(*args, **kwargs):
#         print("Before calling the function.")
#         result = func(*args, **kwargs)
#         print("After calling the function")
#         return result
#     return wrapper

# @smart_wrapper
# def add(a, b,c):
#     return a + b+ c

# print(add(1,3,4))

# def divide_decorator(func):
#     def wrapper(a,b):
#         try:
#              return func(a,b)
#         except ZeroDivisionError:
#             return ("Ooops Denominator cannot be Zero")
#     return wrapper

# @divide_decorator
# def divide(a, b):
#     # print(a/b)
#     return a/b

# print(divide(5,2))

# def star(func):
#     def wrapper(*args, **kwargs):
#         print('*' * 15)
#         func(*args, **kwargs)
#         print('*' * 15)
#     return wrapper

# def dash(func):
#     def wrapper(*args, **kwargs):
#         print('-'*10)
#         func(*args, **kwargs)
#         print('-'*10)
#     return wrapper


# @dash
# @star
# def print_welcome():
#     print("Welcome to the program.")

# print_welcome()

# def funArgs(normal, *args, **kwargs):
#     print("Normal element: ", normal)
#     for ele in args:
#         print(ele)
#     if(len(kwargs) > 0):
#         print("Keyword Argument: ")
#     for key,val in kwargs.items():
#         print(key, " : ", val)

#     for x in kwargs:
#         print(x, kwargs[x])

# other = ['Rohan', 'Simran', 'Raj']
# position_dict = {'name':'Rohan', 'Position': 'Junior Teacher', 'salary': 60000}
# funArgs('Amit', *other, **position_dict)

# class Employee:
#     __slots__ = ['name', 'salary', 'role']
#     no_of_leaves = 8

#     def __init__(self, name, salary, role):
#         self.name = name
#         self.salary = salary
#         self.role = role
    
#     def __str__(self):
#         return f"Name: {self.name}, Salary: {self.salary}, Role: {self.role}"
    

# harry = Employee("Harry", 288, "Instructor")
# rohan = Employee("Rohan", 129, "Supervisor")

# print(harry.no_of_leaves)
# print(rohan.no_of_leaves)

# import inspect

# print(inspect.getmembers(harry))

# import this
# print(this)

# def gen(n):
#     for i in range(n):
#         yield i

# def fibo(x):
#     a, b = 0, 1
#     print(a, b, end=" ")
#     for i in range(x):
#         a, b = b, a+b
#         print(b, end=" ")


# def fiboGen(x):
#     a, b = 0, 1
#     print(a, b, end=" ")
#     for i in gen(x):
#         a, b = b, a+b
#         print(b, end=" ")
# fiboGen(100000)

# def fiboGen(x):
#     a, b, = 0, 1
#     yield a
#     yield b
#     for i in range(x):
#         a, b = b, a+b
#         yield b

# for num in fiboGen(100000):
#     print(num, end=" ")    

# def factGen(x):
#     result = 1
#     for y in range(1, x+1):
#         result *= y
#         yield result

    
# for x in factGen(20):
#     print(x)
    
#Descriptors

# class Ten:
#     def __get__(self, obj, objType=None):
#         return 10
    
# class A:
#     val = 199
#     ten = Ten()

# a = A()
# print(a.val) #Dictionary Lookup
# print(a.ten) #Descriptor lookup

# import os

# class DirectorySize:
#     def __get__(self, obj, objType=None):
#         try:
#             return len(os.listdir(obj.dirname))
#         except FileNotFoundError:
#             return "Wrong Directory name"
            
    
# class A:
#     dl = DirectorySize()
#     def __init__(self, dirname):
#         self.dirname = dirname

# a = A("15. Classes")
# print(a.dl)
# print(a.dirname)

# import logging

# logging.basicConfig(level=logging.INFO)

# class LoggedAgeAccess:
#     def __get__(self, obj, objtype=None):
#         value = obj.__age
#         logging.info(f"Accessing {'age'} giving {value}")
#         return value
    
#     def __set__(self, obj, value):
#         logging.info(f'Updating {'age'} to {value}')
#         obj.__age = value


# class Person:
#     age = LoggedAgeAccess()
#     height = LoggedAgeAccess() # same varible '__age' get edited/accessed.
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height

#     def birthday(self):
#         self.age += 1

# #1. self.age = age in __init__
# #2. → triggers LoggedAgeAccess.__set__(self=descriptor, obj=self(Person), value=age)
# #3. → inside __set__, it does obj.__age = value
# #4. → now the Person instance has a hidden attribute __age

# mary = Person('Mary M', 30, 200)
# mary.name
# mary.age
# mary.age = 100
# print(mary.__dict__)
# mary.birthday()
# john = Person('John S', 19, 180)
# john.age
# mary.age
# mary.height # issue _age is hardwired in LoggedAgeAccess descriptor, therefore it updating and accessing same variable.

#Solution is customized name
# import logging
# logging.basicConfig(level=logging.INFO)

# class LoggedAccess:
#     def __set_name__(self, owner, name):
#         self.public_name = name
#         self.private_name = "_" + name
    
#     def __get__(self, obj, objtype=None):
#         value = getattr(obj, self.private_name)
#         logging.info(f"Accessing {self.public_name} giving {self.private_name}")

#     def __set__(self, obj, value):
#         logging.info(f"Updating {self.public_name} to {value}")
#         setattr(obj, self.private_name, value)

# class Person:
#     name = LoggedAccess()
#     age = LoggedAccess()

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    

# mary = Person('Mary M', 23)

# print(mary.name)
# print(mary.age)
# print(vars(vars(Person)['age']))
# print(vars(Person.__dict__['name']))
# print(vars(mary))
# 
class Yes:
    def __set_name__(self, owner, name):
        self.pub_name = name
        self.priv_name = "__" + name

    def __get__(self, obj, objCls=None):
        print(f"Getting value of {obj} of type {objCls}")
        if obj:
            return getattr(obj, self.priv_name)
        # return getattr(objCls, self.pub_name, "Nothing here")
    
    def __set__(self, obj, value):
        print("Setting...")
        setattr(obj, self.priv_name, value)


class UseDescriptor:
    alpha = Yes() 
    beta = Yes()
    def __init__(self,value, val2):
        self.alpha = value
        self.beta = val2
        
    
dd = UseDescriptor(22,11)
# dd.alpha = "asdf"
print(dd.alpha)
print(dd.beta)
print(dd.__dict__)


""" 
Code:           UseDescriptor dd = UseDescriptor(22, 11)
                     dd.alpha = 22
                      ↓
Python:              obj.alpha = 22  →  finds descriptor "alpha" in class
                      ↓
Descriptor:          Yes.__set__(dd, 22)
                      ↓
Two Variables:       self.pub_name = "alpha"   ← what user sees
                     self.priv_name = "_alpha"  ← where data is stored
                      ↓
Safe Storage:        setattr(obj, self.priv_name, value)  
                     → stores in obj.__dict__ as: _alpha = 22
                      ↓
No Recursion:        obj._alpha is NOT a descriptor  
                     → Python stores directly → no further calls
                      ↓
Access:              dd.alpha → calls __get__ → reads obj._alpha → returns 22
                      ↓
Final State:         dd.__dict__ = {'_alpha': 22, '_beta': 11}
                     dd.alpha = 22 (via descriptor)
"""