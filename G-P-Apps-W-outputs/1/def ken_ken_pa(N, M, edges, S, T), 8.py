
from collections import deque

def ken_ken_pa(N, M, edges, S, T):
    graph = [[] for _ in range(N+1)]
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * (N+1)
    dist = [float('inf')] * (N+1)
    dist[S] = 0

    queue = deque([S])
    while queue:
        current = queue.popleft()
        if current == T:
            return dist[current] // 3

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                dist[neighbor] = dist[current] + 1

    return -1

# Reading input
N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))
S, T = map(int, input().split())

# Call the function and print the result
result = ken_ken_pa(N, M, edges, S, T)
print(result)
```
