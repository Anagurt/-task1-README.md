if len(sys.argv) != 3:
    print("Введите два пути к файлам")
    sys.exit(1)

with open(sys.argv[1]) as f:
    x0, y0 = map(float, f.readline().split())
    r = float(f.readline())

with open(sys.argv[2]) as f:
    for line in f:
        x, y = map(float, line.split())
        d2 = (x - x0) ** 2 + (y - y0) ** 2
        r2 = r ** 2
        if abs(d2 - r2) < 1e-6:
            print(0)
        elif d2 < r2:
            print(1)
        else:
            print(2)
