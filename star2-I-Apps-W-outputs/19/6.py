
from collections import defaultdict
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

n = int(input())
graph = defaultdict(set)
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

result = [0] * (n+1)
for k in range(1, n+1):
    result[k] = len(dfs(graph, k))

print(*result[1:])

