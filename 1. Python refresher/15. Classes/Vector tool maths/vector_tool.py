# FILE: vector_tool.py
from dataclasses import dataclass

"""
SCENARIO: Create a tool for 2D physics/graphics.
INSTRUCTIONS:
1. Use @dataclass to create a 'Vector' with x and y coordinates.
2. Implement '__add__' to allow: vector1 + vector2.
3. Implement '__mul__' to allow: vector * scalar (e.g., Vector(1, 2) * 3).
4. Implement '__repr__' so printing the vector looks like "Vector(x, y)".
5. BONUS: Use '__slots__' in the dataclass to make it memory efficient.
"""
