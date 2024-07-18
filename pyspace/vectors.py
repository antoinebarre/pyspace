

from dataclasses import dataclass


@dataclass
class Vector():
    x: float
    y: float
    z: float

    def __str__(self):
        return f"(x={self.x}, y={self.y}, z={self.z})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __add__(self, other:'Vector'):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other:'Vector'):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other:int | float):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other:int | float):
        return Vector(self.x / other, self.y / other, self.z / other)
    
    def distance(self, other:'Vector'):
        return ((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)**0.5
