from parent import Parent

class Child(Parent):
    def __init__(self):
        super().__init__()
        self._value = 20