
from collections import deque

def solve(grid, stamina):
    n, m = len(grid), len(grid[0])
    start_i, start_j = -1, -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                start_i, start_j = i, j
                break
        if start_i != -1:
            break
    
    queue = deque([(start_i, start_j, 0, stamina)])
    visited = set()
    days = 0
    while queue:
        i, j, cost, stamina = queue.popleft()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        
        if grid[i][j] == 'G':
            return cost
        
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != '#' and (ni, nj) not in visited:
                if grid[ni][nj] == '.':
                    queue.append((ni, nj, cost + 1, stamina - 1))
                elif grid[ni][nj] == 'F':
                    queue.append((ni, nj, cost + 1, stamina - 2))
                elif grid[ni][nj] == 'M':
                    queue.append((ni, nj, cost + 1, stamina - 3))
        
        if stamina <= 0:
            days += 1
            stamina = K
    
    return -1

N, M, K = map(int, input().split())
grid = [input() for _ in range(N)]

print(solve(grid, K))

