
from src.prosta import Line
from src.wektor import Vector
from src.punkt import Point


def test_vector():
    vector = Vector(1, 2, 3)

    assert vector.x == 1
    assert vector.y == 2
    assert vector.z == 3


def test_two_points():
    A = Point(1, 2, 3)
    B = Point(2, 3, 4)

    vector = Vector.two_points(A, B)

    assert vector.x == 1
    assert vector.y == 1
    assert vector.z == 1


def test_from_line():
    point = Point(1, 2, 3)
    vector = Vector(4, 5, 6)
    line = Line(point, vector)

    result = Vector.from_line(line)

    assert result.x == 4
    assert result.y == 5
    assert result.z == 6


def test_add():
    a = Vector(1, 2, 3)
    b = Vector(4, 5, 6)

    result = Vector.add(a, b)

    assert result.x == 5
    assert result.y == 7
    assert result.z == 9


def test_subtract():
    a = Vector(1, 2, 3)
    b = Vector(4, 5, 6)

    result = Vector.subtract(a, b)

    assert result.x == -3
    assert result.y == -3
    assert result.z == -3


def test_new_vector():
    a = Vector(1, 2, 3)
    b = Vector(4, 5, 6)

    result = Vector.new_vector(a, b)

    assert result.x == -3
    assert result.y == 6
    assert result.z == -3
