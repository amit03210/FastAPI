# 1. Basic Import
# Create a file math_utils.py with a function that calculates the square of a number.
...

# In another file main.py, import that function and use it.
...

# Run main.py in VS Code.
...

# 2. Aliasing Imports
# Create a module string_utils.py with a function that reverses a string.
...

# In main.py, import it using an alias (e.g., import string_utils as su).
... 

# Call the function with the alias.
...

# 3. Using __name__ == "__main__"
# Write a module fibo.py that prints Fibonacci numbers when run directly.
...

# But when imported into main.py, it should only provide the function without printing.
...

# 4. Exploring sys.path
# In main.py, print out sys.path.
...
# Add a custom folder to sys.path and place a module there.

# Import that module successfully.
...

# 5. Package Structure
# Create a folder utils/ with two files:
...
# math_ops.py → contains math functions
...
# string_ops.py → contains string functions
...
# Add an __init__.py file inside utils/.

# Import both modules in main.py using from utils import math_ops, string_ops.
...

# 6. FastAPI Integration
# Create a FastAPI app in app.py.
...
# Put your utility functions in a separate module helpers.py.
...
# Import and use those functions inside your FastAPI routes.
...
# 7. dir() Exploration
# Import the math module in main.py.

# Use dir(math) to list all available functions.
...
# Try calling at least two of them.
...

# 8. Custom Module + External Library
# Install an external library (e.g., requests) in your VS Code environment.

# Create a module api_utils.py that uses requests to fetch data.
...
# Import and use it inside main.py.
...
# 9. Relative Imports
# Create a package services/ with two modules:
...
# db.py → simulates a database connection
...
# auth.py → simulates authentication
...
# Use relative imports (from .db import connect) inside auth.py.
...

# 10. Experiment with __pycache__
# Run one of your modules.

# Check the __pycache__ folder created.

# Observe the .pyc file and note its naming convention.
#its convention is modulename.cpython-version.pyc