# EXERCISE 5: The Mystery of __repr__
# Create a class 'Coordinate' with x and y values.
# Implement the __repr__ method so that when you print the object, 
# it looks like: "Coordinate(x=5, y=10)" instead of <__main__.Coordinate object...>.
from coordinate import Coordinate

def main():
    cor1 = Coordinate(24,52)

    print(cor1)

if __name__ == "__main__":
    main()