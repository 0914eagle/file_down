
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set()
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited

r, c = map(int, input().split())
maze = [input() for _ in range(r)]

graph = {}
for i in range(r):
    for j in range(c):
        if maze[i][j] != '#':
            graph[(i, j)] = []
            if i > 0 and maze[i - 1][j] != '#':
                graph[(i, j)].append((i - 1, j))
            if i < r - 1 and maze[i + 1][j] != '#':
                graph[(i, j)].append((i + 1, j))
            if j > 0 and maze[i][j - 1] != '#':
                graph[(i, j)].append((i, j - 1))
            if j < c - 1 and maze[i][j + 1] != '#':
                graph[(i, j)].append((i, j + 1))

joe_pos = (0, 0)
for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            joe_pos = (i, j)
            break
    if joe_pos != (0, 0):
        break

visited = bfs(graph, joe_pos)
if (0, 0) in visited or (r - 1, 0) in visited or (0, c - 1) in visited or (r - 1, c - 1) in visited:
    print(0)
else:
    print("IMPOSSIBLE")

