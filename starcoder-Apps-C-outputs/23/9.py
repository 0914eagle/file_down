
import sys
from collections import deque

speed, deltaT = map(float, input().split())
w, h, x, y = map(int, input().split())

grid = [[0] * w for _ in range(h)]
for row in range(h):
    grid[row] = list(map(int, input().split()))

def is_safe(x, y, t):
    return 0.5 * speed * (abs(grid[y][x]) - abs(grid[y][x] + t)) <= 0

def bfs(x, y):
    queue = deque()
    queue.append((x, y, 0))
    visited = set()
    visited.add((x, y))

    while queue:
        x, y, t = queue.popleft()

        # exceed the time limit
        if t > 12 * 3600:
            break

        # arrive at home
        if x == w - 1 and y == h - 1:
            return t

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny, nt = x + dx, y + dy, t + deltaT
            # out of bound
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            # unsafe
            if not is_safe(nx, ny, nt):
                continue
            # visited
            if (nx, ny) in visited:
                continue
            queue.append((nx, ny, nt))
            visited.add((nx, ny))

    return None

ans = bfs(0, 0)
print(ans)

