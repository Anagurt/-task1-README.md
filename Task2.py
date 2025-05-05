import sys

# Проверяем количество аргументов
if len(sys.argv) != 3:
    print("Введите два пути к файлам")
    sys.exit(1)

# Считываем параметры окружности
with open(sys.argv[1]) as f:
    x0, y0 = map(float, f.readline().split())
    r = float(f.readline())

# Считываем точки и определяем их положение
with open(sys.argv[2]) as f:
    for line in f:
        x, y = map(float, line.split())
        d2 = (x - x0) ** 2 + (y - y0) ** 2
        r2 = r ** 2
        if abs(d2 - r2) < 1e-6:  # На окружности
            print(0)
        elif d2 < r2:            # Внутри
            print(1)
        else:                    # Снаружи
            print(2) 
