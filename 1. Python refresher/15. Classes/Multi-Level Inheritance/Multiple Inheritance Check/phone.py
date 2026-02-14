class Phone:
    def __init__(self, ram, **kwargs):
        self.ram = ram
        super().__init__(**kwargs)

    def make_call(self):
        return f"Making call..."
    
