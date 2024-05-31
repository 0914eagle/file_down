
from collections import deque

def min_ken_ken_pa(N, M, edges, S, T):
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u-1].append(v-1)
    
    dist = [-1] * N
    dist[S-1] = 0
    
    queue = deque([S-1])
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    return dist[T-1]

# Read input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

result = min_ken_ken_pa(N, M, edges, S, T)
print(result)
