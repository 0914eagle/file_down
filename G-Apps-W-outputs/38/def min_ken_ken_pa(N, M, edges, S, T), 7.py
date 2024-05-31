
from collections import deque

def min_ken_ken_pa(N, M, edges, S, T):
    graph = [[] for _ in range(N+1)]
    for u, v in edges:
        graph[u].append(v)
    queue = deque([(S, 0)])
    visited = set()
    
    while queue:
        node, steps = queue.popleft()
        if node == T:
            return steps // 3
        if node in visited:
            continue
        visited.add(node)
        
        for neighbor in graph[node]:
            queue.append((neighbor, steps + 1))
    
    return -1

# Input parsing
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

result = min_ken_ken_pa(N, M, edges, S, T)
print(result)
