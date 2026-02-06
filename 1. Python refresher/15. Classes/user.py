"""
User model for E-Wallet system
"""

class User:
    # - Class attribute to track total users created
    userCount = 0

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        User.userCount += 1

    def __str__(self):
       return f'User has been created {self.name} with user id {self.user_id} and now total user is {User.userCount}'
