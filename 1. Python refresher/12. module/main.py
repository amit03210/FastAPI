import sys
sys.path.append("C:\\Users\\amits\\OneDrive\\Documents\\Python projects")

import math_utils # math_utils.py moved to "Pytho projects" folder
import string_utils as su
import fibo
from utils import math_ops, string_ops
import math
import api_utils
from services import auth

print(math_utils.squares(100))
print(su.reverse_str("Hello Brother"))
fibo.fibo(10)
print(sys.path)
print(math_ops.add(1,90));
print(string_ops.caps("hello"))
print(dir(math))
print(math.factorial(10))
print(math.radians(360))

def run():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    data = api_utils.fetch_json(url)
    print("Fetched text: \n", data)

run()
print(auth.login("admin", "secret")) 
print(auth.login("guest", "1234"))

