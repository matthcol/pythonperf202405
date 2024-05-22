

if __name__ == '__main__':
    points = [
        Point("A", 3, 4), 
        WeightedPoint("B", 5, 6, 10), 
        WeightedPoint("B-", 5, 6, -10),
    ]
    for p in points:
        print(p, end=' -> ')
        p.translate(1, -1)
        print(p)