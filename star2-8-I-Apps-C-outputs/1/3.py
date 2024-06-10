
from collections import deque


def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


N, K, M = map(int, input().split())
graph = {i: set() for i in range(1, N + 1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)

producers = set(range(1, K + 1))
warehouse = set([N])
reachable = bfs(graph, 1)

if not producers.issubset(reachable) or not warehouse.issubset(reachable):
    print(0)
else:
    print(len(producers))


