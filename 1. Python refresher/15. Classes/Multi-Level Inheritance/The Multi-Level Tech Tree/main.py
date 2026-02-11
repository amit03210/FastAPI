# EXERCISE: The Multi-Level Tech Tree
# Create a class 'ElectronicDevice'. 
# Create a child 'Computer' (inherits from ElectronicDevice).
# Create a grandchild 'Laptop' (inherits from Computer).
# Add one unique method to each. Create a Laptop object and call all three methods.

from laptop import Laptop
from computer import Computer
from electronicDevice import ElectronicDevice

def main():
    l1 = Laptop('Lenevo', 2, 10, 4, 500, 2)
    c1 = Computer('Desktop', 3, 15, 10, 1000)
    e1 = ElectronicDevice('Heater', 5, 20)

    print(l1.power_consumption())
    print(c1.power_consumption())
    print(e1.power_consumption())

    print(c1.ram_in_MB())
    print(l1.ram_in_MB())

    print(l1.is_it_portable())

    print(l1)
    print("\n-------------------\n")
    print(c1)
    print("\n-------------------\n")
    print(e1)

if __name__ == "__main__":
    main()
