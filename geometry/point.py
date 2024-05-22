import math

class Point:
    """represents a 2D point with its coordinates x and y
    """
    
     # init method or constructor
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        
    # override both __repr__ and __str__
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
    def distance(self, p):
        return math.sqrt((self.x - p.x)**2 +(self.y - p.y)**2)
    
    def translate(self, deltaX, deltaY):
        self.x += deltaX
        self.y += deltaY
        
if __name__ == '__main__':
    pt1 = Point(12, 34)
    pt2 = Point()
    for p in pt1, pt2:
        print(p)
        print("\t- str: ", str(p))
        print("\t- repr: ", repr(p))
    d = pt1.distance(pt2)
    print("distance:", d)
    pt1.translate(1, -1) # x=13, y=33
    print("after translate:", pt1)
        
    