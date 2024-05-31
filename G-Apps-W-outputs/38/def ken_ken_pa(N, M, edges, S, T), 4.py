
from collections import deque

def ken_ken_pa(N, M, edges, S, T):
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u - 1].append(v - 1)
    
    visited = [False] * N
    dist = [-1] * N
    queue = deque()
    queue.append(S - 1)
    dist[S - 1] = 0

    while queue:
        curr_vertex = queue.popleft()
        visited[curr_vertex] = True

        for neighbor in graph[curr_vertex]:
            if not visited[neighbor]:
                if dist[neighbor] == -1:
                    dist[neighbor] = dist[curr_vertex] + 1
                    queue.append(neighbor)
    
    return dist[T - 1]

# Input processing
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

result = ken_ken_pa(N, M, edges, S, T)
print(result)
