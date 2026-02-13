class Robot:
    modelnumber_temp = 1011

    def __init__(self):
        self.model_number = Robot.modelnumber_temp + 1
        Robot.modelnumber_temp = self.model_number

    