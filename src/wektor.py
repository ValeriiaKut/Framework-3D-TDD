
from src.punkt import Point


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def two_points(cls, A, B):
        return cls(
            B.x - A.x,
            B.y - A.y,
            B.z - A.z
        )

    @classmethod
    def from_line(cls, line):
        return cls(
            line.vector.x,
            line.vector.y,
            line.vector.z
        )

    @classmethod
    def add(cls, a, b):
        return cls(
            a.x + b.x,
            a.y + b.y,
            a.z + b.z
        )

    @classmethod
    def subtract(cls, a, b):
        return cls(
            a.x - b.x,
            a.y - b.y,
            a.z - b.z
        )

    @classmethod
    def new_vector(cls, a, b):
        return cls(
            a.y * b.z - a.z * b.y,
            a.z * b.x - a.x * b.z,
            a.x * b.y - a.y * b.x
        )