import sys

# Проверяем количество аргументов
if len(sys.argv) != 2:
    print("Введите путь к файлу")
    sys.exit(1)

# Считываем числа из файла
with open(sys.argv[1]) as f:
    nums = [int(line) for line in f if line.strip()]

nums.sort()
m = nums[len(nums)//2]  # Медиана
# Считаем сумму модулей разностей
print(sum(abs(x - m) for x in nums)) 
