
from src.prosta import Line
from src.punkt import Point
from src.wektor import Vector


def test_line():
    point = Point(1, 2, 3)
    vector = Vector(5, 6, 7)

    line = Line(point, vector)

    assert line.point == point
    assert line.vector == vector


def test_by_two_points():
    point1 = Point(1, 2, 3)
    point2 = Point(4, 5, 6)

    line = Line.by_two_points(point1, point2)

    assert line.point == point1
    assert line.vector.x == 3
    assert line.vector.y == 3
    assert line.vector.z == 3


def test_by_point_and_vector():
    point = Point(1, 2, 3)
    vector = Vector(4, 5, 6)

    line = Line.by_point_and_vector(point, vector)

    assert line.point == point
    assert line.vector == vector
