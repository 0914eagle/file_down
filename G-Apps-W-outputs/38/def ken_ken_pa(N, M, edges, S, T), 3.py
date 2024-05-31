
from collections import deque

def ken_ken_pa(N, M, edges, S, T):
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u-1].append(v-1)

    visited = [False] * N
    queue = deque([(S-1, 0)])
    visited[S-1] = True

    while queue:
        current_vertex, steps = queue.popleft()

        if current_vertex == T-1:
            return steps // 3

        for neighbor in graph[current_vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, steps+1))

    return -1

# Read input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

result = ken_ken_pa(N, M, edges, S, T)
print(result)
