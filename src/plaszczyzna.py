
import math
from src.wektor import Vector


class Plane:
    def __init__(self, point, normal_vector):
        self.point = point
        self.normal_vector = normal_vector

    @classmethod
    def by_point_and_vector(cls, point, vector):
        return cls(point, vector)

    @classmethod
    def by_three_points(cls, A, B, C):
        AB = Vector.two_points(A, B)
        AC = Vector.two_points(A, C)

        normal = Vector.new_vector(AB, AC)

        return cls(A, normal)

    def distance_to_point(self, point):
        numerator = abs(
            self.normal_vector.x * (point.x - self.point.x) +
            self.normal_vector.y * (point.y - self.point.y) +
            self.normal_vector.z * (point.z - self.point.z)
        )

        denominator = math.sqrt(
            self.normal_vector.x ** 2 +
            self.normal_vector.y ** 2 +
            self.normal_vector.z ** 2
        )

        if denominator == 0:
            raise ValueError("Normal vector cannot be zero")

        return numerator / denominator
