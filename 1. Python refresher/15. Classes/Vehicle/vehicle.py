class Vehicle:
    def __init__(self, name, wheel, seat, color, carType):
        self.name = name
        self.wheel = wheel
        self.seat = seat
        self.color = color
        self.carType = carType

    def start_engine(self):
        return "Rattling noise."
    
    def __str__(self):
        return f"Car name: {self.name}.\nCar Type: {self.carType}.\nWheels: {self.wheel}.\nSeat: {self.seat}.\nColor: {self.color}"
    

