import sys

if len(sys.argv) != 3:
    print("Usage: python task1.py n m")
    sys.exit(1)

n = int(sys.argv[1])
m = int(sys.argv[2])

path = []
visited = set()
current = 0  # индекс (0-based)

while current not in visited:
    path.append(str(current + 1))
    visited.add(current)
    current = (current + m) % n

print(''.join(path)) 
