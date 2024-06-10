
from collections import deque

def bfs(graph, start, target):
    queue = deque([start])
    visited = set()
    while queue:
        curr = queue.popleft()
        if curr in visited:
            continue
        if curr in target:
            return True
        visited.add(curr)
        queue.extend(graph[curr])
    return False

def solve(n, m, k, ores, coals, graph):
    if bfs(graph, 1, ores) and bfs(graph, 1, coals):
        return 2
    elif bfs(graph, 1, ores):
        return 1
    elif bfs(graph, 1, coals):
        return 1
    else:
        return "impossible"

n, m, k = map(int, input().split())
ores = set(map(int, input().split()))
coals = set(map(int, input().split()))
graph = {i: set() for i in range(1, n+1)}
for _ in range(n):
    neighbors = list(map(int, input().split()))
    for neighbor in neighbors[1:]:
        graph[neighbors[0]].add(neighbor)

print(solve(n, m, k, ores, coals, graph))

