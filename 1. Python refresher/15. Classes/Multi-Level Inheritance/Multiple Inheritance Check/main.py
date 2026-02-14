# EXERCISE 5: Multiple Inheritance Check
# Create a class 'Camera' with a 'take_photo' method.
# Create a class 'Phone' with a 'make_call' method.
# Create a class 'Smartphone' that inherits from BOTH.
# Create a smartphone instance and use both features.

from smartphone import SmartPhone

def main():
    samsung = SmartPhone(4,mp= 20)

    print(samsung.make_call())
    print(samsung.take_photo())

if __name__ == "__main__":
    main()