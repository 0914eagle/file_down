
from collections import defaultdict, deque
from sys import stdin, stdout
def bfs(graph, start, end):
    queue = deque([(start, 0)])
    seen = set([start])
    while queue:
        vertex, level = queue.popleft()
        if vertex == end:
            return level
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append((node, level + 1))
    return -1
def solve(n, graph):
    for i in range(n):
        for j in range(n):
            if i != j and bfs(graph, i, j) == -1:
                return "impossible"
    return n
n, m = map(int, stdin.readline().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
stdout.write(str(solve(n, graph)))

