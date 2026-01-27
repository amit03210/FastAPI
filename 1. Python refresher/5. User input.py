"""
Docstring for 1. Python refresher.5. User input
"""

#input()
name = input("Write your name: ")
age = input("What is your age ")

"""
This will throw error because python expected concatenation with + sign.
Because age is stored as string.
print(f"So you were born in {2026-age}") 
"""
# Lesson: input is always string

# To convert input to int or float we use int() or float() function
age = int(input("What is your age "))
print(f"So you were born in {2026-age} or close") 


#======================excercise==============================
# 1. Write a program that asks for your name and prints a greeting.
# Expected behavior:
# Input: Alice
# Output: Hello, Alice!

name = input("Excercise 1: Write name \n")
print(f"Hello, {name}")

# 2. Ask the user for their age and print how old they’ll be in 5 years.
# Expected behavior:
# Input: 20
# Output: In 5 years, you will be 25.

age = int(input(f"what is your age, {name}\n"))
print(f"So after 5 years you'll be {age + 5} years old.")

# 3. Ask the user for a number, then show both the string version and the integer version.
# Expected behavior:
# Input: 42
# Output: As string: "42"
#         As integer: 42
randomNumber = input("Any random number ")
print(f"As string: \"{randomNumber}\"")
print(f"As integer: {int(randomNumber)}")