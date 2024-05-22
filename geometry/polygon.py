from point import Point
from shape import Shape


class Polygon:
    """a shape with vertices (at least 3)
    """
    
if __name__ == '__main__':
    pA = Point.from_coords(1, 2)
    pB = Point.from_coords(4, 2)
    pC = Point.from_coords(4, 6)
    tABC = Polygon(name="ABC", pA, pB, pC)
    print(tABC)
    tABC.translate(1, -1)
    print(tABC)