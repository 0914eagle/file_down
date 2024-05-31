
from collections import deque

def ken_ken_pa(graph, start, end):
    visited = [False] * len(graph)
    queue = deque([(start, 0)])

    while queue:
        current, steps = queue.popleft()
        visited[current] = True

        if current == end:
            return steps // 3

        if steps % 3 == 0:
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    queue.append((neighbor, steps + 1))

    return -1

# Read input
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)

S, T = map(int, input().split())

# Find the minimum number of ken-ken-pa needed
result = ken_ken_pa(graph, S-1, T-1)

# Print the result
print(result)
