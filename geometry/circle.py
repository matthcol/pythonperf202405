from typing import override
from mesurable import Mesurable2D
from point import Point
from shape import Shape

class Circle(Shape, Mesurable2D):
    
    def __init__(self, name: str|None, center: Point, radius: float):
        super().__init__(name)
        self.center = center
        self.radius = radius
        
    # since python 3.12: @override
    @override
    def __repr__(self) -> str:
        return f"Circle(name={self.name}, center={self.center}, radius={self.radius})"
    
    @override
    def translate(self, deltaX: float, deltaY: float):
        self.center.translate(deltaX, deltaY)
    

if __name__ == "__main__":
    p = Point.from_coords(3, 4)
    c = Circle(name="C", center=p, radius=10.0)
    print(c)
    c.translate(1, -1)
    print(c)