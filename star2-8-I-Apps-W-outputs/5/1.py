
from collections import deque

n, m, k = map(int, input().split())
grid = [list(input()) for i in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == "X":
            start_i = i
            start_j = j

def is_valid(i, j):
    return 0 <= i < n and 0 <= j < m and grid[i][j] != "*"

def bfs(i, j, k):
    queue = deque([(i, j, "", 0)])
    visited = set()
    while queue:
        i, j, path, length = queue.popleft()
        if (i, j) in visited:
            continue
        if length == k:
            return path
        visited.add((i, j))
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if is_valid(x, y):
                queue.append((x, y, path+["D", "U", "R", "L"][["S", "N", "E", "W"].index(grid[i][j])], length+1))
    return "IMPOSSIBLE"

print(bfs(start_i, start_j, k))

