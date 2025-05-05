import sys
import json

# Проверяем количество аргументов
if len(sys.argv) != 4:
    print("Введите три пути к файлам")
    sys.exit(1)

# Загружаем значения по id
with open(sys.argv[1], encoding='utf-8') as f:
    values = {v['id']: v['value'] for v in json.load(f)['values']}

# Загружаем структуру тестов
with open(sys.argv[2], encoding='utf-8') as f:
    data = json.load(f)

# Рекурсивно заполняем value
def fill(d):
    if isinstance(d, list):
        for x in d:
            fill(x)
    elif isinstance(d, dict):
        if 'id' in d and d['id'] in values:
            d['value'] = values[d['id']]
        if 'values' in d:
            fill(d['values'])

fill(data)

# Сохраняем результат
with open(sys.argv[3], 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2) 
