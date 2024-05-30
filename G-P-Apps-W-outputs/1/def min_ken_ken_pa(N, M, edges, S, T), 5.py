
from collections import deque

def min_ken_ken_pa(N, M, edges, S, T):
    graph = {i: [] for i in range(1, N + 1)}
    for u, v in edges:
        graph[u].append(v)

    min_steps = [-1] * (N + 1)
    min_steps[S] = 0

    queue = deque([S])

    while queue:
        current_vertex = queue.popleft()

        for next_vertex in graph[current_vertex]:
            if min_steps[next_vertex] == -1 or min_steps[next_vertex] > min_steps[current_vertex] + 1:
                min_steps[next_vertex] = min_steps[current_vertex] + 1
                queue.append(next_vertex)

    return min_steps[T]

# Reading input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

# Calling the function
result = min_ken_ken_pa(N, M, edges, S, T)

# Printing the result
print(result)
```
