
from collections import defaultdict, deque

def ken_ken_pa(N, M, edges, S, T):
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
    
    queue = deque([(S, 0)])
    visited = set()
    
    while queue:
        curr_node, steps = queue.popleft()
        
        if curr_node == T:
            return steps // 3
        
        for neighbor in graph[curr_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))
    
    return -1

# Input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

# Output
result = ken_ken_pa(N, M, edges, S, T)
print(result)
