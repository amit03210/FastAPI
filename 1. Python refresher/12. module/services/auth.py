from .db import connect

def login(user: str, password:str):
    db_status = connect()
    if user == "admin" and password == "secret": 
        return f"{db_status} User {user} authenticated!" 
    else: 
        return f"{db_status} Authentication failed for {user}."