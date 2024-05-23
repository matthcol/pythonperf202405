import re

class Point:
    
    # froze list of attributes
    __slots__ = [ '_name', '_x', '_y' ]
    
    def __init__(self, name: str|None=None, x: float=0.0, y: float=0.0):
        self.name = name # use setter
        self._x = x
        self._y = y
        
    @property
    def name(self) -> str|None:
        """name of this point"""
        return self._name
    
    @name.setter
    def name(self, value: str|None):
        if value is None:
            self._name  = None
        elif re.fullmatch(r"[\s]*", value):
            raise ValueError("name must contain at least one visible character or be None")
        else:
            self._name = value.strip()
    
    @property
    def x(self) -> float:
        "horizontal coordinate of this point"
        return self._x
    
    @x.setter
    def x(self, value: float):
        self._x = value
        
    @property
    def y(self) -> float:
        "vertical coordinate of this point"
        return self._y
    
    @y.setter
    def y(self, value: float):
        self._y = value
    
    def __repr__(self) -> str:
        return f"Point(name={self.name}, x={self.x}, y={self.y})"
    
    
if __name__ == '__main__':
    p1 = Point()
    p2 = Point("A", 1, 2)
    for p in p1, p2:
        print(p)
        print("\tx =", p.x)
        p.x += 3
        p.name = " \tB  \n\r "
        print(p)
        print()
    
    # p3 = Point(name="")
    # del p1.name
    p1.note = "beautiful point"