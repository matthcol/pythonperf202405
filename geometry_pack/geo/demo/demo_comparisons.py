import operator
from geo.data import Point, WeightedPoint

p1 = Point("A", 1, 2)
p2 = Point("B", 3, 4)
p3 = p1
p1bis = Point("A", 1, 2)
p4 = WeightedPoint("Aw", 1, 2, 10)

print(p1 is p2)
print(p1 is p1)
print(p1 is p3)
print(p1 is p1bis)
print()
print(p1 == p2)
print(p1 == p1)
print(p1 == p3)
print(p1 == p1bis)
print()
print(p1 == "A")
print("A" == p1)
print()
print(p1 != p1bis)
print()
print(p1 == p4, p4 == p1)
print()
list_point = [ p1, p2 ]
print("in list:", p1bis in list_point)
set_point = { p1, p2 }
set_point.add(p4)
print(p1bis, "in set", set_point, ":", p1bis in set_point)
dict_point = {
    p1: p1.name,
    p2: p2.name,
    p4: p4.name
}
print("in dict:", p1 in dict_point)

list_point.extend((p4, p1bis, Point.from_coords(1, -1)))
list_point.sort()
print(list_point)
list_point.sort(key=lambda p: p.name if p.name else '')
print(list_point)
list_point2 = sorted(list_point, key=operator.attrgetter('y', 'x'))
print(list_point2)
print(p1 < p2) # TypeError (by default)
print(p1 > p2)
print(p1 <= p2)
print(p1 >= p2)