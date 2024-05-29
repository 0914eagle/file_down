
from collections import defaultdict, deque

def kahn_topological_sort(n, edges):
    graph = defaultdict(list)
    in_degrees = [0] * n
    
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        in_degrees[v] += 1
    
    sources = deque([node for node in range(n) if in_degrees[node] == 0])
    max_source_size = max(len(sources), 1)
    
    while sources:
        node = sources.popleft()
        for neighbor in graph[node]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                sources.append(neighbor)
                max_source_size = max(max_source_size, len(sources))

    return max_source_size

# Input parsing
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Output the largest possible size of S
print(kahn_topological_sort(n, edges))
```
