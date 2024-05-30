
import math
from collections import defaultdict

def bitwise_or_path(graph, start, end):
    visited = set()
    stack = [(start, 0)]
    while stack:
        node, path = stack.pop()
        if node == end:
            return path
        visited.add(node)
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                stack.append((neighbor, path | weight))

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    print(bitwise_or_path(graph, s, t))

# Sample Input
# 4 7
# 1 2 1
# 1 2 3
# 1 3 2
# 1 4 1
# 2 3 4
# 2 4 4
# 3 4 4
# 3
# 1 2
# 1 3
# 3 4

# Sample Output
# 1
# 2
# 3
```
