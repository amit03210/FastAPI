# EXERCISE 5: The Double-Dunder Mix-up
# Create a variable named __my_var__ (two underscores on both sides).
# Check if Python mangles this name. 
# (Hint: Python only mangles if it DOES NOT end with double underscores).

from parent import Parent
import parent

def main():
    p1 = Parent()

    print(p1.__my_var__) #works, no mangling
    print(p1._Parent__only_leading_underscore) #name mangling happened
    
    print(parent.__newspaper)  #works, module variable

if __name__ == "__main__":
    main()


