
from dataclasses import dataclass, field


@dataclass(kw_only=True, slots=True, order=True)
class Point:
    name: str|None = field(default=None, compare=False)
    x: float = 0.0
    y: float = 0.0
    
if __name__ == '__main__':
    p1 = Point()
    p2 = Point(name="A", x=3, y=4) # Point("A", 3, 4)
    p3 = Point(name="B", x=5, y=7)
    p2bis = Point(name="_A", x=3, y=4)
    for p in p1, p2, p3:
        print(p)
    assert p2 == p2bis
    assert p2 < p3
    assert p2 <= p3