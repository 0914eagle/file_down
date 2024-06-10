
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
a = list(map(int, input().split()))
visited = bfs(graph, 1)
if len(visited) != n:
    print("No")
else:
    for i in range(n):
        if a[i] not in graph[a[i]]:
            print("No")
            break
    else:
        print("Yes")

