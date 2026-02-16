# EXERCISE 1: The Safe Calculator
# Create a function 'safe_divide(a, b)'. 
# Use a try-except block to handle ZeroDivisionError.
# If an error occurs, return 0. Otherwise, return the result.

def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 0
    except TypeError:
        return '--'
    
print(safe_divide(1,0))
