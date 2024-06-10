
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    used = set([start])
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in used:
                used.add(neighbor)
                queue.append(neighbor)
    return used


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

a = list(map(int, input().split()))
used = bfs(graph, 1)
if len(used) != n:
    print("No")
else:
    if a == list(used):
        print("Yes")
    else:
        print("No")

