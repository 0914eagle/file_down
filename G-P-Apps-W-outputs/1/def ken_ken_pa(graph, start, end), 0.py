
from collections import deque

def ken_ken_pa(graph, start, end):
    n = len(graph)
    visited = [False] * n
    queue = deque([(start, 0)])
    
    while queue:
        node, steps = queue.popleft()
        visited[node] = True
        
        if node == end:
            return steps // 3
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append((neighbor, steps + 1))
    
    return -1

# Read input
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)

S, T = map(int, input().split())

# Call the function
result = ken_ken_pa(graph, S-1, T-1)

# Print result
print(result)
```
