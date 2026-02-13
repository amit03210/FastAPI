from robot import Robot

class CleaningRobot(Robot):
    def __init__(self, dustbin_capacity):
        super().__init__()
        self.dustbin_capacity = dustbin_capacity

    def __str__(self):
        return f"Serial number: {self.model_number} Dustbin Capacity of {self.dustbin_capacity} Kg"