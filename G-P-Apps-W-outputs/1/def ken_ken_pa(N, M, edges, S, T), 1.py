
from collections import deque

def ken_ken_pa(N, M, edges, S, T):
    graph = {i: [] for i in range(1, N+1)}
    for u, v in edges:
        graph[u].append(v)
    
    queue = deque([(S, 0)])
    visited = set()
    
    while queue:
        curr, count = queue.popleft()
        
        if curr == T:
            return count // 3
        
        visited.add(curr)
        
        if count % 3 == 0:
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    queue.append((neighbor, count+1))
        else:
            queue.append((curr, count+1))
    
    return -1

# Read input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

# Call the function and print the result
result = ken_ken_pa(N, M, edges, S, T)
print(result)
```
