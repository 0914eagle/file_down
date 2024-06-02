
import random

def expected_meeting_time(n, m, neighbours, s, t):
    graph = {i: set() for i in range(n)}
    for u, v in neighbours:
        graph[u].add(v)
        graph[v].add(u)

    def bfs(start):
        visited = set()
        queue = [(start, 0)]
        while queue:
            node, time = queue.pop(0)
            if node == t:
                return time
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, time + 1))
        return float('inf')

    min_time = min(bfs(s), bfs(t))
    if min_time == float('inf'):
        return "never meet"
    else:
        return min_time

# Input parsing
n, m = map(int, input().split())
neighbours = [tuple(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

# Output
print(expected_meeting_time(n, m, neighbours, s, t))
