class Camera:
    def __init__(self, mega_pixel, **kwargs):
        self.MB = mega_pixel
        super().__init__(**kwargs)
        
    def take_photo(self):
        return "Smile 3...2..1...Clickkk"
    