from typing import override
from mesurable import Mesurable2D
from point import Point
from shape import Shape


class Polygon(Shape, Mesurable2D):
    """a shape with vertices (at least 3)
    """
    
    def __init__(self, *vertices: Point, name: str|None,):
        super().__init__(name)
        self.vertices = vertices
        
    @override
    def __repr__(self) -> str:
        return f"Polygon(name={
                self.name
            }, vertices count={
                len(self.vertices)
            } vertices={
                "-".join((v.name if v.name else "?") for v in self.vertices)
            })"

    @override
    def translate(self, xDelta: float, yDelta: float):
        for vertice in self.vertices:
            vertice.translate(xDelta, yDelta)
    
if __name__ == '__main__':
    pA = Point(name="A", x=1, y=2)
    pB = Point(name="B", x=2, y=2)
    pC = Point.from_coords(4, 6)
    tABC = Polygon(pA, pB, pC, name="ABC")
    vertices=(pB, pC, pA)
    tBCA = Polygon(*vertices, name="BCA")
    print(tABC)
    tABC.translate(1, -1)
    print(tABC)
    print(tBCA)