
from sys import stdin
from itertools import product

def solve(n, m, grid):
    max_time = 0
    max_grid = None
    for i, j in product(range(n), range(m)):
        if grid[i][j] == 'X':
            time = max(i, n - i - 1, j, m - j - 1)
            if time > max_time:
                max_time = time
                max_grid = [['X' if (i - time <= x <= i + time and j - time <= y <= j + time) else '.' for y in range(m)] for x in range(n)]
    return max_time, max_grid

n, m = map(int, stdin.readline().split())
grid = [list(stdin.readline().strip()) for _ in range(n)]
max_time, max_grid = solve(n, m, grid)
print(max_time)
for row in max_grid:
    print(''.join(row))

