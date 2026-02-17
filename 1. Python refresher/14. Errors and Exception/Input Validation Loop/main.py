# EXERCISE 2: Input Validation Loop
# Write a 'while' loop that asks the user for their age using input().
# Use try-except to catch ValueError if they type a string (like "twenty").
# The loop should keep asking until a valid integer is entered.

while True:
    try:
        age = int(input("Enter you age: "))
        break #Break loop when enter value int value 
    except ValueError:
        print("Please write value age in numberical value.")


