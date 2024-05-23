from functools import total_ordering
import math
from collections.abc import Iterable, Iterator
from typing import Self

from shape import Shape

@total_ordering
class Point(Shape, Iterable):
    """represents a 2D point with its coordinates x and y
    """
    
     # init method or constructor
    def __init__(self, name: str|None=None, x: float=0.0, y: float=0.0):
        super().__init__(name)
        self.x = x
        self.y = y
        
    # override both __repr__ and __str__
    def __repr__(self) -> str:
        return f"Point(name={self.name}, x={self.x}, y={self.y})"
    
    def __iter__(self) -> Iterator:
        return iter((self.x, self.y))
    
    # operators == and !=
    def __eq__(self, other: object) -> bool:
        # opt: selfand other are the same object
        if self is other:
            return True
        # test on other: isinstance, type, hasattr
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)
    
    # if p1 == p2 then hash(p1) == hash(p2)
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) < (other.x, other.y)
    
    def __add__(self, other: object) -> Self:
        if type(other) in (int, float):
            return Point.from_coords(self.x + other, self.y + other)
        elif isinstance(other, Point):
            return Point.from_coords(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented
        
    def __radd__(self, other: object) -> Self:
        return self.__add__(other)
    
    def __iadd__(self, other: object) -> Self:
        if type(other) in (int, float):
            self.x += other
            self.y += other
        elif isinstance(other, Point):
            self.x += other.x
            self.y += other.y
        else:
            return NotImplemented
        return self
    
    def distance(self, p: Self) -> float:
        return math.hypot(self.x - p.x, self.y - p.y)
    
    def translate(self, deltaX: float, deltaY: float):
        self.x += deltaX
        self.y += deltaY
        
    @classmethod
    def from_coords(cls, x: float, y: float) -> "Point":
        return cls(x=x, y=y)

def demo_inheritance():
    pt1 = Point(x=12, y=34)
    print(pt1, "is an instance of class Point:", isinstance(pt1, Point))
    print(pt1, "is an instance of class object:", isinstance(pt1, object))
    print(pt1, "is an instance of abstract class Iterable:", isinstance(pt1, Iterable))
    print(pt1, "is an instance of classes object, Iterable, Point:", 
          isinstance(pt1, (object, Iterable, Point)))
    
def demo_iterable():
    pt1 = Point(name="A", x=12, y=34)
    print("Coordinates of:", pt1)
    for coord in pt1:
        print("\t-", coord)
        
if __name__ == '__main__':
    pt1 = Point(x=12, y=34)
    pt2 = Point()
    for p in pt1, pt2:
        print(p)
        print("\t- str: ", str(p))
        print("\t- repr: ", repr(p))
    d = pt1.distance(pt2)
    print("distance:", d)
    pt1.translate(1, -1) # x=13, y=33
    print("after translate:", pt1)
    # pt3 = Point("aa", False)
    # print(pt3)
    # print(pt1.distance(pt3))
    demo_inheritance()
    demo_iterable()
    
    print(Point.__mro__)
    
        
    