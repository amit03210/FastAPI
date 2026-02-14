# ================================
# 📝 Python Functions Practice Sheet (Blank)
# ================================

# -------------------------------
# Level 1: Defining Functions
# -------------------------------

# 1. Define a function that prints "Hello, World".
# Call the function.
def greet():
    print("Hello, World")

greet()

# 2. Define a function that takes a name as argument and prints "Hello <name>".
# Call it with your name.
def greet_name(name):
    print(f"Hello {name}")

greet_name("Alice")

# 3. Define a function that adds two numbers and returns the result.
# Test it with 5 and 7.
def add(x, y):
    return x+y

print(add(23, 1))

# -------------------------------
# Level 2: Default & Keyword Arguments
# -------------------------------

# 4. Define a function greet(name, greeting="Hello") that prints "<greeting>, <name>".
# Call it with and without the greeting argument.
def greet(name, greeting="Hello"):
    print(greeting, name)

greet("Rahul")
greet("Raj", greeting = "Namaste")

# 5. Define a function power(base, exponent=2) that returns base raised to exponent.
# Test with power(3), power(3, 3).
def power(base, exponent=2):
    return base ** exponent
print(power(3))
print(power(3,3))

# -------------------------------
# Level 3: Return Values & Scope
# -------------------------------

# 6. Define a function that returns the maximum of three numbers.
# Test with 10, 20, 15.
def max_number(*value):
    return max(value)
print(max(10,20,15))

# 7. Define a function that uses a local variable and prints it.
# Try printing the variable outside the function (should cause an error).
def anime():
    anime_name = "DBZ"
    print(anime_name)

# print(anime_name)

# -------------------------------
# Level 4: Variable Arguments
# -------------------------------

# 8. Define a function that takes any number of arguments (*args) and returns their sum.
# Test with 3, 5, 7, 9.
def sum_of_n_number(*value):
    return sum(value)
print(sum_of_n_number(3, 5, 7, 9,542))

# 9. Define a function that takes keyword arguments (**kwargs) and prints them.
# Call with name="Alice", age=25.
def data(**kwargs):
    print(kwargs)
print(data(name="Alice", age = 25))
# -------------------------------
# Level 5: Nested & Lambda Functions
# -------------------------------

# 10. Define a function outer() that defines an inner() function and calls it.
# Test the behavior.
def outer():
    def inner():
        print("inner")
    return inner

fc = outer()
fc()

# 11. Write a lambda function that multiplies two numbers.
# Test with 4 and 6.
multiply = lambda x,y: x *y
print(multiply(54,2))
# -------------------------------
# Level 6: Higher-order Functions
# -------------------------------

# 12. Define a function apply_twice(func, value) that applies a function to a value twice.
# Example: apply_twice(lambda x: x*2, 5) → 20
def add_twice(func, y):
    return func(func(y))

print(add_twice(lambda x: x+1, 6))

# 13. Use map() with a lambda to square a list of numbers [1, 2, 3, 4].
squares =   list(map(lambda x:x*x, range(1,5)));
print(squares)

# 14. Use filter() with a lambda to keep only even numbers from [1, 2, 3, 4, 5, 6].
even = list(filter(lambda x: x%2==0, range(1,11)))
print(even)
# -------------------------------
# Challenge Exercises
# -------------------------------

# 15. Define a recursive function factorial(n).
# Test with 5.
def fact(n):
    if n<=1:
        return 1
    return n * fact(n-1)
print(fact(5))

# 16. Define a function fibonacci(n) that returns the nth Fibonacci number.
# Test with 7.
def fibo(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)
print(fibo(7))

# 17. Define a function that returns another function (closure) which adds a fixed number.
# Example: make_adder(5) → returns a function that adds 5 to its input.

def make_adder(y):
    def adder(x):
        return y+x;
    return adder;

x = make_adder(10)
print(x);
print(x(12))

#1. Positional and Default argument
# Exercise 1
def power(base, exponent=2):
    print(base**exponent)

# Test cases
power(5)        # Expected: 25
power(2, 3)     # Expected: 8

#2. Keyword default argument
# Exercise 2
def introduce(name, country="India", language="Python"):
    print(f"My name is {name}, I'm from {country}, and I love {language}")

# Test cases
introduce("Alice")
introduce(language="JavaScript", name="Bob", country="USA")

#3. Variable-length argument
# Exercise 3
def average(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    print(sum//len(numbers))

# Test cases
average(10, 20, 30)   # Expected: 20
average(5, 15)        # Expected: 10

#Arbitrary keyword argument
# Exercise 4
def profile(**details):
    for x, y in details.items():
        print(x, y)

# Test cases
profile(name="Alice", age=25, hobby="Coding")

"""
Write a function student_info that:
- Takes a name (positional argument).
- Has a default argument for course="Python".
- Accepts any number of skills using *args.
- Accepts extra details like age, city, etc. using **kwargs.
"""

def student_info(name, course="Python", *skills, **extra):
    print(f"Name: {name}")
    print(f"Course: {course}")
    for x, y in extra.items():
        print(x + ":" + str(y))
    print("Skills:", end=" ")
    print(*skills, sep=", ")
student_info("Alice", "Data Science", "SQL", "Machine Learning", age=25, city="Lucknow")

#Challenge: Write a function order_test that has all four types of arguments and prints them in order. Then call it with:

def order_test( pos, defA=20, *args, **kwargs):
    print(f"Positiona: {pos}")
    print(f"Default: {defA}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

order_test(10,99,30,40, 50, key1="A", key2="B")

def mixed_args(a, b, c=5, d=10, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

mixed_args(1, 2, 3, 4, 5, 6, x=100, y=200)

def order_pizza(pizza_size, crust="thin", *toppings, **kwargs):
    print(f"Size: {pizza_size}")
    print(f"Crust: {crust}") 
    print(f"Toppings: {toppings}")
    print(f"Details: {kwargs}")

order_pizza("Large", "Cheese Burst", "Olives", "Mushrooms", "Peppers", delivery_time="8 PM", address="Lucknow")

