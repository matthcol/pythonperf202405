from circle import Circle
from mesurable import Mesurable2D
from point import Point
from polygon import Polygon
from weightedpoint import WeightedPoint

shapes = [
    Point("A", 3.0, 4.0),
    Point("B", 6.0, 7.0),
    WeightedPoint("C", -8.0, 9.0, 2.0),
    Circle("C1", Point(), 10.0),
    Polygon(Point(), Point(), Point(), name='ABC')
]

# first round
for shape in shapes:
    match shape:
        case Point(name=name, x=x, y=y):
            print(f"Point detected: name={name}, x={x}, y={y}")
print()

# second round
for shape in shapes:
    match shape:
        case WeightedPoint(name=name, x=x, y=y, weight=weight):
            print(f"WeightedPoint detected: name={name}, x={x}, y={y} weight={weight}")
        case Point(name=name, x=x, y=y):
            print(f"Point detected: name={name}, x={x}, y={y}")
print()

# second round
for shape in shapes:
    match shape:
        case Point(name="A", x=x, y=y):
            print(f"Point A detected: name={name}, x={x}, y={y}")
        case Point(name=name, x=x, y=y) if x >= 0:
            print(f"Point detected with positive x: name={name}, x={x}, y={y}")
        case Point(name=name, x=x, y=y):
            print(f"Point detected: name={name}, x={x}, y={y}")
        case Mesurable2D() as mesurable:
            s = mesurable.surface()
            p = mesurable.perimeter()
            print(f"Mesurable shape: name={shape.name}, perimeter={p}, surface={s}")
print()

match shapes:
    case []:
        print("No shapes")
    case [shape]:
        print("only one shape")
    case [Point() as p, *others]:
        print("1st element is a point")
        print(f" - point: name={p.name}, x={p.x}, y={p.y}")
        print(" - others:", others)
    case _:
        print("list begining with a non-point shape and at least 2 elements")
