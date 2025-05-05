import sys
import math

# Функция для чтения параметров окружности из файла
# Возвращает координаты центра (x, y) и радиус
def read_circle_params(file_path):
    with open(file_path, 'r') as file:
        center_line = file.readline().strip()
        radius_line = file.readline().strip()
        
        center_x, center_y = map(float, center_line.split())
        radius = float(radius_line)
        
        return (center_x, center_y), radius

# Функция для чтения точек из файла
# Возвращает список кортежей (x, y)
def read_points(file_path):
    with open(file_path, 'r') as file:
        points = []
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
        return points

# Функция для определения положения точки относительно окружности
# 0 — на окружности, 1 — внутри, 2 — снаружи
def determine_position(circle_center, radius, point):
    cx, cy = circle_center
    px, py = point
    
    distance_squared = (px - cx)**2 + (py - cy)**2
    radius_squared = radius**2
    
    # math.isclose используется для сравнения с учётом погрешности вычислений
    if math.isclose(distance_squared, radius_squared, rel_tol=1e-9):
        return 0  # На окружности
    elif distance_squared < radius_squared:
        return 1  # Внутри окружности
    else:
        return 2  # Снаружи окружности

# Главная функция программы
def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py circle_file points_file")
        return
    
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    
    try:
        circle_center, radius = read_circle_params(circle_file)
        points = read_points(points_file)
        
        for point in points:
            position = determine_position(circle_center, radius, point)
            print(position)
            
    except FileNotFoundError:
        print("Error: One or both input files not found")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
