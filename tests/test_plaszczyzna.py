
from src.plaszczyzna import Plane
from src.punkt import Point
from src.wektor import Vector


def test_plane():
    point = Point(1, 2, 3)
    normal = Vector(0, 0, 1)

    plane = Plane(point, normal)

    assert plane.point == point
    assert plane.normal_vector == normal


def test_by_point_and_vector():
    point = Point(1, 2, 3)
    normal = Vector(0, 0, 1)

    plane = Plane.by_point_and_vector(point, normal)

    assert plane.point == point
    assert plane.normal_vector.x == 0
    assert plane.normal_vector.y == 0
    assert plane.normal_vector.z == 1


def test_by_three_points():
    A = Point(1, 1, 1)
    B = Point(3, 1, 1)
    C = Point(1, 3, 1)

    plane = Plane.by_three_points(A, B, C)

    assert plane.point == A
    assert plane.normal_vector.x == 0
    assert plane.normal_vector.y == 0
    assert plane.normal_vector.z == 4


def test_distance_to_point():
    plane = Plane(
        Point(1, 2, 3),
        Vector(0, 0, 1)
    )

    point = Point(1, 2, 8)

    assert plane.distance_to_point(point) == 5
