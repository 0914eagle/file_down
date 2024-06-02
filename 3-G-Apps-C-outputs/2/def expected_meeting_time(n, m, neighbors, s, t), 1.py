
import random

def expected_meeting_time(n, m, neighbors, s, t):
    graph = [[] for _ in range(n)]
    for u, v in neighbors:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start):
        visited = [False] * n
        queue = [(start, 0)]
        visited[start] = True

        while queue:
            node, time = queue.pop(0)
            if node == t:
                return time
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, time + 1))

        return -1

    time = bfs(s)
    if time == -1:
        return "never meet"
    else:
        return time

# Input
n, m = map(int, input().split())
neighbors = [tuple(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

# Output
print(expected_meeting_time(n, m, neighbors, s, t))
