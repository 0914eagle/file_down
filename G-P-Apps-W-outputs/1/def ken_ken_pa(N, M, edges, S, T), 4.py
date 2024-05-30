
from collections import deque

def ken_ken_pa(N, M, edges, S, T):
    adj_list = [[] for _ in range(N+1)]
    for u, v in edges:
        adj_list[u].append(v)

    dist = [-1] * (N+1)
    dist[S] = 0
    q = deque([S])

    while q:
        current = q.popleft()
        for neighbor in adj_list[current]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[current] + 1
                q.append(neighbor)

    return dist[T]

# Input processing
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

result = ken_ken_pa(N, M, edges, S, T)
print(result)
```
