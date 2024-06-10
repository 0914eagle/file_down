
from collections import deque
def solve(n, m, volcanoes):
    grid = [[0] * (n + 1) for _ in range(n + 1)]
    for x, y in volcanoes:
        grid[x][y] = 1
    queue = deque([(1, 1, 0)])
    visited = set()
    while queue:
        x, y, time = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if x == n and y == n:
            return time
        if x < n and grid[x + 1][y] == 0:
            queue.append((x + 1, y, time + 1))
        if y < n and grid[x][y + 1] == 0:
            queue.append((x, y + 1, time + 1))
    return -1
n, m = map(int, input().split())
volcanoes = [tuple(map(int, input().split())) for _ in range(m)]
print(solve(n, m, volcanoes))

