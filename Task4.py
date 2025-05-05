import sys

# Функция для вычисления минимального количества ходов,
# чтобы все элементы массива стали равны (через медиану)
def min_moves_to_equal_elements(nums):
    nums.sort()  # Сортируем массив
    median = nums[len(nums) // 2]  # Находим медиану
    # Суммируем абсолютные разности каждого элемента и медианы
    return sum(abs(num - median) for num in nums)

def main():
    if len(sys.argv) != 2:
        print("Usage: python program.py input_file.txt")
        return
    
    try:
        # Считываем числа из файла, по одному в строке
        with open(sys.argv[1], 'r') as file:
            nums = [int(line.strip()) for line in file if line.strip()]
        
        if not nums:
            print("Error: Input file is empty")
            return
        
        moves = min_moves_to_equal_elements(nums)
        print(moves)
    
    except FileNotFoundError:
        print(f"Error: File {sys.argv[1]} not found")
    except ValueError:
        print("Error: Input file contains non-integer values")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
