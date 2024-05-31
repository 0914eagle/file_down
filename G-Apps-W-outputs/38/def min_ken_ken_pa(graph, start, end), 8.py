
from collections import deque

def min_ken_ken_pa(graph, start, end):
    visited = [False] * len(graph)
    distance = [float('inf')] * len(graph)
    distance[start] = 0
    queue = deque([start])

    while queue:
        current = queue.popleft()
        visited[current] = True

        for neighbor in graph[current]:
            if not visited[neighbor]:
                distance[neighbor] = min(distance[neighbor], distance[current] + 1)
                queue.append(neighbor)

    return distance[end] if distance[end] != float('inf') else -1

# Input processing
N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)

S, T = map(int, input().split())

result = min_ken_ken_pa(graph, S-1, T-1)
print(result)
