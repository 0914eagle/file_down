
from collections import defaultdict
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return visited

def solve(n, graph):
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        controlled = bfs(graph, i)
        result[len(controlled)] = max(result[len(controlled)], len(controlled))
    return result[1:]

n = int(input())
graph = defaultdict(set)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

result = solve(n, graph)
print(*result)

