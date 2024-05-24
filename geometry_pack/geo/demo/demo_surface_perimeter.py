from typing import List
from geo.data import Circle, Mesurable2D, Point, Polygon, WeightedPoint, Shape


pA = Point(name="A", x=1, y=2)
pB = Point(name="B", x=2, y=2)
pC = Point.from_coords(4, 6)
tABC = Polygon(pA, pB, pC, name="ABC")
c1 = Circle(name="C1", center=pA, radius=10.0)
c2 = Circle(name="C2", center=pB, radius=8.0)

shapes: List[Shape] = [
    pA, 
    pB, 
    pC, 
    tABC,
    c1,
    c2
]

for s in shapes:
    print(s)
    if isinstance(s, Mesurable2D):
        surface = s.surface()
        perimeter = s.perimeter()
        print(f"\t * surface= {surface}, perimeter={perimeter}")