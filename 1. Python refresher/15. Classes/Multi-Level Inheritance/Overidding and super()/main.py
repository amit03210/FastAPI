# Overriding and super()
# Create a class 'Robot' with an __init__ that sets a 'model_number'.
# Create a child 'CleaningRobot' that has its own __init__.
# Inside CleaningRobot's __init__, use super() to set the model_number, 
# and then manually set a new attribute 'dust_bin_capacity'.

from cleaningrobot import CleaningRobot

def main():
    hitachi = CleaningRobot(2)
    samsung = CleaningRobot(1.5)
    lenovo = CleaningRobot(3.5)

    print(hitachi)
    print(lenovo)
    print(samsung)

if __name__ == '__main__':
    main()