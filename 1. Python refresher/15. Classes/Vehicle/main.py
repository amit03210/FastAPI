# EXERCISE 4: Inheritance Challenge
# Create a parent class 'Vehicle' with a method 'start_engine'.
# Create a child class 'ElectricCar' that inherits from Vehicle.
# Override 'start_engine' in ElectricCar to print something different 
# (like "Silent start...").

from electricCar import ElectricCar
from vehicle import Vehicle

def main():
    car1 = ElectricCar('Tesla', 4, 2, 'red', 'sedan')
    car2 = Vehicle("Toyota", 4, 6, 'Gray', 'Jeep')

    print(car2.start_engine())
    print("\n====================\n")
    print(car1)
    print(car1.start_engine())

if __name__ == "__main__":
    main()