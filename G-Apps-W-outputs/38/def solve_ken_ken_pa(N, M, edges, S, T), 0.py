
from collections import deque

def solve_ken_ken_pa(N, M, edges, S, T):
    graph = {i: [] for i in range(1, N+1)}
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * (N+1)
    count = 0

    queue = deque([(S, 0)])
    while queue:
        current_vertex, steps = queue.popleft()
        
        if current_vertex == T:
            return steps // 3
        
        if visited[current_vertex]:
            continue
        
        visited[current_vertex] = True
        
        for neighbor in graph[current_vertex]:
            queue.append((neighbor, steps + 1))
    
    return -1

# Read input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

# Call the function and output the result
result = solve_ken_ken_pa(N, M, edges, S, T)
print(result)
