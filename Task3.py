import json
import sys

# Функция для загрузки данных из JSON-файла
def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Функция для сохранения данных в JSON-файл
def save_json_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

# Рекурсивная функция для заполнения поля 'value' в структуре отчёта
# tests_structure — структура отчёта (dict или list)
# values_dict — словарь соответствий id -> value
def fill_values(tests_structure, values_dict):
    if isinstance(tests_structure, list):
        # Если это список, обрабатываем каждый элемент
        for item in tests_structure:
            fill_values(item, values_dict)
    elif isinstance(tests_structure, dict):
        # Если есть id и он есть в values_dict — заполняем value
        if 'id' in tests_structure and tests_structure['id'] in values_dict:
            tests_structure['value'] = values_dict[tests_structure['id']]
        # Если есть вложенные значения — рекурсивно обрабатываем их
        if 'values' in tests_structure:
            fill_values(tests_structure['values'], values_dict)

def main():
    if len(sys.argv) != 4:
        print("Usage: python program.py values.json tests.json report.json")
        return

    try:
        # Получаем пути к файлам из аргументов командной строки
        values_path = sys.argv[1]
        tests_path = sys.argv[2]
        report_path = sys.argv[3]

        # Загружаем данные из файлов
        values_data = load_json_file(values_path)
        tests_data = load_json_file(tests_path)

        # Создаём словарь для быстрого доступа к значениям по id
        values_dict = {item['id']: item['value'] for item in values_data['values']}

        # Копируем структуру tests, чтобы не изменять исходные данные
        report_data = json.loads(json.dumps(tests_data))

        # Заполняем значения в структуре отчёта
        fill_values(report_data, values_dict)

        # Сохраняем отчёт в файл
        save_json_file(report_data, report_path)

        print(f"Report successfully generated and saved to {report_path}")

    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in input files")
    except KeyError as e:
        print(f"Error: Missing required field in JSON - {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
