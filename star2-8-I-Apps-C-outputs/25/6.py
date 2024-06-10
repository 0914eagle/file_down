
import sys
from collections import deque


def bfs(graph, start, end):
    queue = deque([start])
    visited = set()
    while queue:
        node = queue.popleft()
        visited.add(node)
        if node == end:
            return True
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
    return False


n, m, k = map(int, input().split())
ore = set(map(int, input().split()))
coal = set(map(int, input().split()))
graph = {i: [] for i in range(1, n + 1)}
for i in range(1, n + 1):
    a, *neighbours = map(int, input().split())
    graph[i] = neighbours

min_settlers = 1
for i in range(1, n + 1):
    if bfs(graph, 1, i) and i in ore:
        min_settlers += 1
        break
for i in range(1, n + 1):
    if bfs(graph, 1, i) and i in coal:
        min_settlers += 1
        break

if min_settlers == 3:
    print(min_settlers)
else:
    print("impossible")

