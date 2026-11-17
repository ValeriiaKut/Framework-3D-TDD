
from src.wektor import Vector


class Line:
    def __init__(self, point, vector):
        self.point = point
        self.vector = vector

    @classmethod
    def by_two_points(cls, point1, point2):
        AB = Vector(
            point2.x - point1.x,
            point2.y - point1.y,
            point2.z - point1.z
        )
        return cls(point1, AB)

    @classmethod
    def by_point_and_vector(cls, point, vector):
        return cls(point, vector)
