
from collections import deque


def steel_age(n, m, k, ore, coal, graph):
    visited = [False] * (n + 1)
    queue = deque([1])
    visited[1] = True
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
    if all(visited[i] for i in ore) and all(visited[i] for i in coal):
        return 1
    queue = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
    if all(visited[i] for i in ore) and all(visited[i] for i in coal):
        return 2
    return "impossible"


n, m, k = map(int, input().split())
ore = list(map(int, input().split()))
coal = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    neighbors = list(map(int, input().split()))
    for j in range(1, neighbors[0] + 1):
        graph[i].append(neighbors[j])
print(steel_age(n, m, k, ore, coal, graph))

