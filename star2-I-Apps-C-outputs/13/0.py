
import sys
from collections import deque

def bfs(grid, start, end, stamina):
    queue = deque([start])
    visited = set([start])
    days = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if (x, y) == end:
                return days
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                    if grid[nx][ny] != '#':
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        days += 1
    return -1

def main():
    n, m, k = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    start, end = None, None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                end = (i, j)
    cost = {'S': 0, 'F': 1, 'M': 2, '.': 1}
    stamina = k
    days = 0
    while stamina > 0:
        days = bfs(grid, start, end, stamina)
        if days == -1:
            print(-1)
            return
        stamina -= cost[grid[start[0]][start[1]]]
    print(days)

if __name__ == '__main__':
    main()

