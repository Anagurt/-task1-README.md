import sys

# Проверяем количество аргументов
if len(sys.argv) != 3:
    print("Введите два числа: n m")
    sys.exit(1)

n = int(sys.argv[1])  # Размер массива
m = int(sys.argv[2])  # Длина интервала

arr = list(range(1, n + 1))  # Массив от 1 до n
result = ""
i = 0  # Начинаем с первого элемента

while True:
    result += str(arr[i])  # Добавляем текущий элемент к результату
    i = (i + m - 1) % n    # Переходим к следующему элементу по кругу
    if i == 0:              # Если вернулись к началу — заканчиваем
        break

print(result) 
