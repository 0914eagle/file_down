
from collections import deque

def ken_ken_pa(N, M, edges, S, T):
    graph = {i: [] for i in range(1, N+1)}
    for u, v in edges:
        graph[u].append(v)

    dist = {i: float('inf') for i in range(1, N+1)}
    dist[S] = 0

    queue = deque([S])
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if dist[neighbor] > dist[current] + 1:
                dist[neighbor] = dist[current] + 1
                queue.append(neighbor)

    if dist[T] == float('inf'):
        return -1
    else:
        return dist[T] // 3

# Sample Input
N = 4
M = 4
edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
S = 1
T = 3

print(ken_ken_pa(N, M, edges, S, T))
```
