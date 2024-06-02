
from collections import defaultdict

def expected_meeting_time(n, m, neighbors, s, t):
    graph = defaultdict(list)
    for u, v in neighbors:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, target, steps):
        if node == target:
            return steps
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                result = dfs(neighbor, target, steps + 1)
                if result != -1:
                    return result
        return -1

    visited = set()
    visited.add(s)
    visited.add(t)
    result = dfs(s, t, 0)
    if result != -1:
        return result
    return "never meet"

# Input
n, m = map(int, input().split())
neighbors = [tuple(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

# Output
print(expected_meeting_time(n, m, neighbors, s, t))
