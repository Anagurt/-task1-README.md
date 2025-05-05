import sys
from decimal import Decimal, getcontext

getcontext().prec = 50  # для работы с большими и малыми числами

if len(sys.argv) != 3:
    print("Usage: python task2.py circle.txt points.txt")
    sys.exit(1)

circle_file = sys.argv[1]
points_file = sys.argv[2]

with open(circle_file) as f:
    x0, y0 = map(Decimal, f.readline().split())
    r = Decimal(f.readline().strip())

with open(points_file) as f:
    points = [tuple(map(Decimal, line.split())) for line in f if line.strip()]

for x, y in points:
    dist2 = (x - x0) ** 2 + (y - y0) ** 2
    r2 = r ** 2
    if dist2 == r2:
        print(0)
    elif dist2 < r2:
        print(1)
    else:
        print(2) 
