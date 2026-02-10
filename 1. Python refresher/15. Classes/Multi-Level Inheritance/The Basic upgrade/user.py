class User:

    UserOnline = 0;

    def __init__(self, name, userId):
        self.name = name
        self.userid = userId
        self.isLogin = False

    def login(self):
        if not self.isLogin:
            self.isLogin = True
            User.UserOnline += 1
            return f"{self.name} has been login in successfully..."
        else:
            return f"{self.name} is already logged in."
    
    def logout(self):
        if self.isLogin:
            User.UserOnline -= 1
            self.isLogin = False
            return f"{self.name} has been logout in successfully..."
        else:
            return f"{self.name} is not logged in yet."
    
    def __str__(self):
        return f"User name: {self.name}\nUser ID: {self.userid}"
    

