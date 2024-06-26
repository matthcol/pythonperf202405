import math
from typing import override
from mesurable import Mesurable2D
from point import Point
from shape import Shape

class Circle(Shape, Mesurable2D):
    
    def __init__(self, name: str|None, center: Point, radius: float):
        super().__init__(name)
        # assert radius > 0, "radius must be > 0"
        if radius <= 0:
            raise ValueError(f"radius must be > 0: {radius}")
        self.center = center
        self.radius = radius
        
    # since python 3.12: @override
    @override
    def __repr__(self) -> str:
        return f"Circle(name={self.name}, center={self.center}, radius={self.radius})"
    
    @override
    def translate(self, deltaX: float, deltaY: float):
        self.center.translate(deltaX, deltaY)
        
    @override
    def surface(self) -> float:
        return math.pi * self.radius**2
    
    
    @override 
    def perimeter(self) -> float:
        return 2.0 * math.pi * self.radius
        
    

if __name__ == "__main__":
    p = Point.from_coords(3, 4)
    c = Circle(name="C", center=p, radius=10.0)
    print(c)
    c.translate(1, -1)
    print(c)
    
    # bad usages:
    
    # c2 = Circle("C2", center= p, radius = -1)
    c.radius = -1
    print(c)
    # c.radius = "not a radius" # error for type checker
    c.note = "beautiful circle"
    print(c, c.note)
    del c.radius
    print(c) # AttributeError: 'Circle' object has no attribute 'radius'