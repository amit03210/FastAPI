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

def star(func):
    def wrapper(*args, **kwargs):
        print('*' * 15)
        func(*args, **kwargs)
        print('*' * 15)
    return wrapper

def dash(func):
    def wrapper(*args, **kwargs):
        print('-'*10)
        func(*args, **kwargs)
        print('-'*10)
    return wrapper


@dash
@star
def print_welcome():
    print("Welcome to the program.")

print_welcome()