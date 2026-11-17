from src.punkt  import Point
import math

def test_point():
    point = Point(2, 3, 4)

    assert point.x == 2
    assert point.y == 3
    assert point.z == 4

def test_distance():
    point1 = Point(1, 2, 0)
    point2 = Point(3, 2, 0)

    assert point1.distance(point2) == 2

