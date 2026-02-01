from fastapi import FASTAPI
import helpers

app = FASTAPI()

@app.get("/")
def root():
    return {"message": "Hello FastAPI is runninggg"}

@app.get("/greet/{name}")
def greet_user(name: str):
    return {"greeting": helpers.greet(name)}

@app.get("/add") 
def add(a: int, b: int): 
    result = helpers.add_numbers(a, b) 
    return {"result": result}