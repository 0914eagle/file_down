
from collections import deque

def ken_ken_pa(N, M, edges, S, T):
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u-1].append(v-1)

    visited = [False] * N
    queue = deque([(S-1, 0)])  # (vertex, ken-ken-pa count)

    while queue:
        curr_vertex, ken_count = queue.popleft()

        if curr_vertex == T-1:
            return ken_count // 3

        if visited[curr_vertex]:
            continue
        
        visited[curr_vertex] = True

        for next_vertex in graph[curr_vertex]:
            queue.append((next_vertex, ken_count + 1))

    return -1

# Read input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

# Call the function with input values
result = ken_ken_pa(N, M, edges, S, T)

# Print the result
print(result)
