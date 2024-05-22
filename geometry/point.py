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
        
if __name__ == '__main__':
    pt1 = Point(12, 34)
    pt2 = Point()
    for p in pt1, pt2:
        print(p)
        print("\t- str: ", str(p))
        print("\t- repr: ", repr(p))
        
    