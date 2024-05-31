
from collections import deque

def ken_ken_pa(N, M, edges, S, T):
    graph = {i: [] for i in range(1, N+1)}
    for u, v in edges:
        graph[u].append(v)
    
    visited = [False] * (N+1)
    distance = [-1] * (N+1)
    
    queue = deque([(S, 0)])  # (vertex, distance)
    visited[S] = True
    distance[S] = 0
    
    while queue:
        current, dist = queue.popleft()
        
        if current == T:
            return dist // 3
        
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = dist + 1
                queue.append((neighbor, dist + 1))
    
    return -1

# Sample Input
N, M = 4, 4
edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
S, T = 1, 3

# Sample Output
print(ken_ken_pa(N, M, edges, S, T))
