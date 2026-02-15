# EXERCISE 1: The Accidental Overwrite
# Create a class 'Parent' with an attribute self._value = 10.
# Create a 'Child' that sets self._value = 20.
# Create a 'Child' object and see what the parent's value is now.
# (This shows why single underscores don't prevent overrides).

from child import Child

def main():
    ch = Child()

    print(ch._value)

if __name__ == "__main__":
    main()