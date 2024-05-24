from geo.data import Point


p = Point("A", 1, 2)
p2 = Point("B", 4, 5)
p += 2 # __iadd__
p += p2 # __iadd__
p3 = p + p2 # __add__
p4 = p + 3 # __add__
p5 = 3 + p # __radd__
for pt in p, p2, p3, p4:
    print(pt)