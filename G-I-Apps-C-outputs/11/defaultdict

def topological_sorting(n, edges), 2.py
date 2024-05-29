
from collections import defaultdict

def topological_sorting(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n
    for edge in edges:
        graph[edge[0]].append(edge[1])
        indegree[edge[1]] += 1
    
    sources = [node for node in range(n) if indegree[node] == 0]
    max_source_count = 0
    
    while sources:
        source = sources.pop(0)
        max_source_count = max(max_source_count, len(sources))
        for neighbor in graph[source]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                sources.append(neighbor)
    
    return max_source_count

# Reading input
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Outputting the result
print(topological_sorting(n, edges))
```
