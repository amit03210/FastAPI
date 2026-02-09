from vehicle import Vehicle

class ElectricCar(Vehicle):
    def __init__(self, name, wheel, seat, color, carType):
        super().__init__(name, wheel, seat, color, carType)

    def start_engine(self):
        return "Since I'm electric I make no noise."