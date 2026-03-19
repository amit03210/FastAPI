# EXERCISE 4: Generator Expressions
# Similar to list comprehensions, you can make generators in one line.
# Example: gen = (x*x for x in range(10))
# Create a generator expression that squares only the odd numbers in a range.

n = 100
sq_gen = (x*x for x in range(n) if x%2!=0)

for x in sq_gen:
    print(x)