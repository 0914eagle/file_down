
from collections import deque

def min_ken_ken_pa(N, M, edges, S, T):
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u-1].append(v-1)

    dist = [-1] * N
    dist[S-1] = 0

    queue = deque([S-1])
    while queue:
        node = queue.popleft()
        if node == T-1:
            return dist[node] // 3

        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return -1

# Input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

# Output
result = min_ken_ken_pa(N, M, edges, S, T)
print(result)
```
