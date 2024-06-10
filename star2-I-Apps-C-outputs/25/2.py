
from sys import stdin
from collections import deque

def bfs(n, m, volcanoes):
    queue = deque([(1, 1, 0)])
    visited = set([(1, 1)])
    while queue:
        x, y, time = queue.popleft()
        if (x, y) == (n, n):
            return time
        if (x + 1, y) not in visited and (x + 1, y) not in volcanoes and x + 1 <= n:
            queue.append((x + 1, y, time + 1))
            visited.add((x + 1, y))
        if (x, y + 1) not in visited and (x, y + 1) not in volcanoes and y + 1 <= n:
            queue.append((x, y + 1, time + 1))
            visited.add((x, y + 1))
    return -1

n, m = map(int, stdin.readline().split())
volcanoes = set()
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    volcanoes.add((x, y))
print(bfs(n, m, volcanoes))

