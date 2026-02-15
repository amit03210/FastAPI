from shape import Shape

class Square(Shape):
    def __init__(self):
        super().__init__()

    def print_color(self):
        # print(self.__color)
        print(self._Shape__color)
