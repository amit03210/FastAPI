# FILE: vector_tool.py
"""
SCENARIO: Create a tool for 2D physics/graphics.
INSTRUCTIONS:
1. Use @dataclass to create a 'Vector' with x and y coordinates.
2. Implement '__add__' to allow: vector1 + vector2.
3. Implement '__mul__' to allow: vector * scalar (e.g., Vector(1, 2) * 3).
4. Implement '__repr__' so printing the vector looks like "Vector(x, y)".
5. BONUS: Use '__slots__' in the dataclass to make it memory efficient.
"""
from dataclasses import dataclass
@dataclass(slots=True)
class Vector:
    '''Class for getting vectors'''
    x: float
    y: float

    def __add__(self,other):
        if self.__class__ is other.__class__:
            return Vector(self.x+other.x, self.y+other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x*scalar, self.y*scalar)
    

vec1 = Vector(1,2)
vec2 = Vector(2,3)

print(vec1+vec2)
print(vec2*4)
print(vec2)

