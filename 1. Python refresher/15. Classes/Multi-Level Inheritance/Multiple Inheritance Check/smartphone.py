from phone import Phone
from camera import Camera

class SmartPhone(Phone, Camera):
    def __init__(self, ram, mp):
        super().__init__(ram = ram, mega_pixel = mp)
    


