# EXERCISE 2: The Mangling Test
# Create a class 'Car' with a private attribute '__engine_code'.
# Try to print my_car.__engine_code directly.
# Then, use dir(my_car) to find the "real" mangled name and print that.

from car import Car

def main():
    my_car = Car(541)

    # print(my_car.__engine_code)
    print(dir(my_car))
    print(my_car._Car__engine_code)

if __name__ == '__main__':
    main()