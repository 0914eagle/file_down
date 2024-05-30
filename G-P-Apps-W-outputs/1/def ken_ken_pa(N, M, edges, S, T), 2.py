
from collections import deque

def ken_ken_pa(N, M, edges, S, T):
    graph = [[] for _ in range(N+1)]
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * (N+1)
    dist = [float('inf')] * (N+1)
    dist[S] = 0

    queue = deque()
    queue.append(S)

    while queue:
        node = queue.popleft()
        if node == T:
            return dist[T] // 3

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return -1

# Read input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

# Call the function and print the result
result = ken_ken_pa(N, M, edges, S, T)
print(result)
```
