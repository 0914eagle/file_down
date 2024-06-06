
from collections import defaultdict
n,m = map(int, input().split())
graph = defaultdict(list)
visited = [0 for _ in range(n)]
for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append([y,z])
def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i[0]] == 0:
            dfs(i[0])
    visited[v] = 2
dfs(0)
count = 0
for i in range(n):
    if visited[i] == 1:
        count += 1
print(count)
