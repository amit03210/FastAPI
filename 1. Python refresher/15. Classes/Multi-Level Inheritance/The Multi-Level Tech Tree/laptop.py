from computer import Computer

class Laptop(Computer):
    def __init__(self,name, amphere, voltage, ram, disk_storage, weight):
        super().__init__(name, amphere, voltage, ram, disk_storage)
        self.weight = weight

    def is_it_portable(self):
        if self.weight < 2:
            return "Yes"
        else:
            return "No"
        
    def __str__(self):
        return f"This laptop has weight of about {self.weight} KG"