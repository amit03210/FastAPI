class ElectronicDevice:
    def __init__(self,name, amphere, voltage):
        self.name = name
        self.amphere = amphere
        self.voltage = voltage

    def power_consumption(self):
        self.watts = self.amphere * self.voltage
        return self.watts
    
    def __str__(self):
        return f"The power consumption of {self.name} is {self.watts} watts"