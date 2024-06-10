
from collections import deque

def solve(grid, stamina):
    n, m = len(grid), len(grid[0])
    q = deque()
    q.append((0, 0, stamina))
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    days = 0
    while q:
        size = len(q)
        for _ in range(size):
            i, j, curr_stamina = q.popleft()
            if grid[i][j] == 'G':
                return days
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < m and not visited[x][y] and grid[x][y] != '#':
                    cost = 1 if grid[x][y] == '.' else 2 if grid[x][y] == 'F' else 3
                    if curr_stamina >= cost:
                        q.append((x, y, curr_stamina - cost))
                        visited[x][y] = True
        days += 1
    return -1

n, m, k = map(int, input().split())
grid = [list(input()) for _ in range(n)]
print(solve(grid, k))

