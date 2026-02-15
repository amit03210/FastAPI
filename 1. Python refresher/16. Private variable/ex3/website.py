class Website:
    def __init__(self):
        pass

    def __connect_to_db(self):
        return f"Connected to Database..."

    def show_page(self):
        print(self.__connect_to_db())
        return f"Loading Page...."