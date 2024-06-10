
import sys

def dfs(start, end):
visited[start] = True
if start == end:
return 1
count = 0
for i, weight in graph[start]:
if not visited[i]:
count += dfs(i, end)
return count

def bfs(start, end):
visited = [False] * V
queue = [start]
visited[start] = True
while queue:
v = queue.pop(0)
if v == end:
return
for i, weight in graph[v]:
if not visited[i]:
visited[i] = True
queue.append(i)

V, E = map(int, input().split())
graph = [[] for _ in range(V)]
for _ in range(E):
u, v, w = map(int, input().split())
graph[u].append((v, w))
s, t = map(int, input().split())

visited = [False] * V
bfs(s, t)
count = dfs(s, t)
print(count)

