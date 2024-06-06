
from collections import deque

n, m, k = map(int, input().split())

iron = list(map(int, input().split()))
coal = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    a = list(map(int, input().split()))
    for j in range(1, a[0] + 1):
        graph[i].append(a[j])

def bfs(graph, start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        s = queue.popleft()
        for i in graph[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return visited

visited = bfs(graph, 1)

iron_count = 0
coal_count = 0

for i in range(1, n + 1):
    if visited[i]:
        if i in iron:
            iron_count += 1
        if i in coal:
            coal_count += 1

if iron_count == 0 or coal_count == 0:
    print("impossible")
else:
    print(iron_count + coal_count - 1)
