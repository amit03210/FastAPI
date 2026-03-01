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

class Employee:
    __slots__ = ['name', 'salary', 'role']
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    
    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}, Role: {self.role}"
    

harry = Employee("Harry", 288, "Instructor")
rohan = Employee("Rohan", 129, "Supervisor")

print(harry.no_of_leaves)
print(rohan.no_of_leaves)
