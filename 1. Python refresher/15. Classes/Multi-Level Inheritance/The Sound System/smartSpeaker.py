from speaker import Speaker

class SmartSpeaker(Speaker):
    def __init__(self,max_vol, normal_vol, wifi_name):
        super().__init__(max_vol, normal_vol)
        self.wifi_name = wifi_name

    def play(self):
        print(f"Connecting to wifi {self.wifi_name}...")
        return super().play()
    