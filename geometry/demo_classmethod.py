from point import Point
from weightedpoint import WeightedPoint

p1 = Point.from_coords(1, 2)
p2 = WeightedPoint.from_coords(3, 4)
print(p1)
print(p2)

bary = WeightedPoint.barycenter(
    WeightedPoint(x=1, y=2, weight=1),
    WeightedPoint(x=9, y=6, weight=3)
)
print(bary)