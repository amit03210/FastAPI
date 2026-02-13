class Speaker:
    def __init__(self, max_volume, normal_volume):
        self.max_volume = max_volume
        self.normal_volume = normal_volume
        if self.max_volume < self.normal_volume:
            raise Exception

    def play(self):
        return f"Player the song at {self.normal_volume} volume"