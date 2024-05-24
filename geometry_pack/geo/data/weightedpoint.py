from .point import Point
from typing import List, cast

class WeightedPoint(Point):
    """add weight to a point
    """ 
    def __init__(self, name: str|None=None, x: float=0, y: float=0, weight: float=0):
        super().__init__(name, x, y)
        self.weight = weight

    def __repr__(self) -> str:
        return f"WeightedPoint(name={self.name}, x={self.x}, y={self.y}, weight={self.weight})"

    @staticmethod
    def barycenter(*weightedpoints: "WeightedPoint") -> "WeightedPoint":
        weight = sum(pt.weight for pt in weightedpoints)
        x_mean = sum(pt.weight * pt.x for pt in weightedpoints) / weight
        y_mean = sum(pt.weight * pt.y for pt in weightedpoints) / weight
        return WeightedPoint(x=x_mean, y=y_mean, weight=weight)
        
    
if __name__ == '__main__':
    points: List[Point] = [
        Point("A", 3, 4), 
        WeightedPoint("B", 5, 6, 10), 
        WeightedPoint("B-", 5, 6, -10),
    ]
    for p in points:
        # mypy assign type Point to var p
        print(p, end=' -> ')
        p.translate(1, -1)
        print(p)
        if isinstance(p, WeightedPoint):
            # mypy assign now type WeightedPoint to var p
            # (type narrowing)
            print("\t* weight =", p.weight) 
            wp = cast(WeightedPoint, p)    
        # back to type Point for var p
        