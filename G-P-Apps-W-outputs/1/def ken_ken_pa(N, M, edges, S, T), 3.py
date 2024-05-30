
from collections import deque

def ken_ken_pa(N, M, edges, S, T):
    graph = [[] for _ in range(N+1)]
    for u, v in edges:
        graph[u].append(v)
    
    dist = [-1] * (N + 1)
    dist[S] = 0
    queue = deque([S])

    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[curr] + 1
                queue.append(neighbor)

    return dist[T]

# Input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

# Output
result = ken_ken_pa(N, M, edges, S, T)
print(result)
```
