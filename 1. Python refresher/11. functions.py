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

# 14. Use filter() with a lambda to keep only even numbers from [1, 2, 3, 4, 5, 6].

# -------------------------------
# Challenge Exercises
# -------------------------------

# 15. Define a recursive function factorial(n).
# Test with 5.

# 16. Define a function fibonacci(n) that returns the nth Fibonacci number.
# Test with 7.

# 17. Define a function that returns another function (closure) which adds a fixed number.
# Example: make_adder(5) → returns a function that adds 5 to its input.
