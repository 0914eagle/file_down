
import sys

n = int(sys.stdin.readline().strip())
grid = [sys.stdin.readline().strip() for _ in range(n)]

def is_triple(x, y, dx, dy):
    return (grid[x][y] != '.' and grid[x+dx][y+dy] != '.' and grid[x+2*dx][y+2*dy] != '.' and
            grid[x][y] == grid[x+dx][y+dy] == grid[x+2*dx][y+2*dy])

count = 0
for x in range(n-2):
    for y in range(n-2):
        for dx, dy in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            if is_triple(x, y, dx, dy):
                count += 1

print(count)

