import sys

# Проверяем количество аргументов командной строки
if len(sys.argv) != 3:
    print("Usage: python task1.py n m")
    sys.exit(1)

# Считываем значения n и m из аргументов
n = int(sys.argv[1])
m = int(sys.argv[2])

path = []           # Список для хранения пути
visited = set()     # Множество для отслеживания посещённых индексов
current = 0         # Текущий индекс (0-based, то есть первый элемент — 0)

# Двигаемся по круговому массиву, пока не вернёмся к уже посещённому элементу
while current not in visited:
    path.append(str(current + 1))  # Добавляем номер элемента (1-based)
    visited.add(current)           # Отмечаем индекс как посещённый
    current = (current + m) % n    # Переходим к следующему элементу по кругу

# Выводим путь в виде строки без пробелов
print(''.join(path)) 
