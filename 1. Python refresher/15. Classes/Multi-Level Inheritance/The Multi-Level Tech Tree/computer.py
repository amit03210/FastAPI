from electronicDevice import ElectronicDevice

class Computer(ElectronicDevice):
    def __init__(self,name, amphere, voltage, ram, disk_storage):
        super().__init__(name, amphere, voltage)
        self.ram = ram
        self.disk_storage = disk_storage

    def ram_in_MB(self):
        return f"RAM in mb is {self.ram*1024}."
    
    def __str__(self):
        return f"{self.name} has {self.ram} GB Ram and {self.disk_storage} GB storage space, and consume {self.power_consumption()} Watts"