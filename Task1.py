import sys

# Функция для построения пути по круговому массиву
# n — размер массива, m — длина интервала
# Возвращает строку с последовательностью начальных элементов интервалов

def circular_path(n, m):
    arr = list(range(1, n+1))  # Формируем массив от 1 до n
    path = []
    current = 0  # Начинаем с первого элемента (индекс 0)
    
    while True:
        # Добавляем текущий начальный элемент в путь
        path.append(str(arr[current]))
        
        # Вычисляем индекс следующего начального элемента по кругу
        current = (current + m - 1) % n
        
        # Если вернулись к первому элементу — завершаем цикл
        if current == 0:
            break
    
    return ''.join(path)

# Главная функция программы
def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py n m")
        return
    
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        
        # Проверяем, что n и m — положительные целые числа
        if n < 1 or m < 1:
            print("Error: n and m must be positive integers")
            return
        
        result = circular_path(n, m)
        print(result)
        
    except ValueError:
        print("Error: n and m must be integers")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
