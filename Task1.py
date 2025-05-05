import sys

if len(sys.argv) != 3:
    print("Введите два числа: n m")
    sys.exit(1)

n = int(sys.argv[1])
m = int(sys.argv[2])

arr = list(range(1, n + 1))
result = ""
i = 0

while True:
    result += str(arr[i])
    i = (i + m - 1) % n
    if i == 0:
        break

print(result)
