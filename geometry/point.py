import math
from collections.abc import Iterable, Iterator
from typing import Self

from shape import Shape

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
    
    def distance(self, p: Self) -> float:
        return math.hypot(self.x - p.x, self.y - p.y)
    
    def translate(self, deltaX: float, deltaY: float):
        self.x += deltaX
        self.y += deltaY

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
    
        
    