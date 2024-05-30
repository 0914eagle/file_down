
from collections import defaultdict

def ken_ken_pa(N, M, edges, S, T):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * (N + 1)
    distances = [float('inf')] * (N + 1)
    distances[S] = 0

    stack = [(S, 0)]
    while stack:
        node, distance = stack.pop()
        visited[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if distance + 1 < distances[neighbor]:
                    distances[neighbor] = distance + 1
                    stack.append((neighbor, distance + 1))

    if distances[T] == float('inf'):
        return -1
    else:
        return distances[T] // 3

# Read input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

# Call the function and print the result
result = ken_ken_pa(N, M, edges, S, T)
print(result)
```
