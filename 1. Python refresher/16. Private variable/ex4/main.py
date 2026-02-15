# EXERCISE 4: Subclassing with Private Vars
# Create a class 'Shape' with self.__color = "Red".
# Create a subclass 'Square'. 
# Try to create a method in Square called 'print_color' that prints self.__color.
# Why does it fail? How can you fix it without using the mangled name?

from square import Square

def main():
    sq = Square()
    sq.print_color()

if __name__ == "__main__":
    main()