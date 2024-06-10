
import sys
from collections import deque

def spread_water(grid):
    N, M = len(grid), len(grid[0])
    queue = deque()
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'V':
                queue.append((i, j))
    while queue:
        i, j = queue.popleft()
        if i > 0 and grid[i-1][j] == '.':
            grid[i-1][j] = 'V'
            queue.append((i-1, j))
        if i < N-1 and grid[i+1][j] == '.':
            grid[i+1][j] = 'V'
            queue.append((i+1, j))
        if j > 0 and grid[i][j-1] == '.':
            grid[i][j-1] = 'V'
            queue.append((i, j-1))
        if j < M-1 and grid[i][j+1] == '.':
            grid[i][j+1] = 'V'
            queue.append((i, j+1))

    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    N, M = map(int, input().split())
    grid = [list(input()) for _ in range(N)]
    spread_water(grid)


