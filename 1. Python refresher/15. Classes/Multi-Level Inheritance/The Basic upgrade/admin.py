from user import User

class Admin(User):
    def delete_user(self):
        User.UserOnline -= 1
        return f"{self.name} has been deleted."
    
    def __repr__(self): #for Console print
        return f"{self.name} user has Admin Status"
    
    def __str__(self): #for print()
        return f"{self.name} has Admin privilage."