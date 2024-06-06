
from sys import stdin
import collections

def bfs(source,graph):
    visited = [0]*(n+1)
    queue = collections.deque([source])
    visited[source] = 1
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if visited[u]==0:
                visited[u]=1
                queue.append(u)
    return visited

n = int(stdin.readline())
graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
    data = list(map(int,stdin.readline().split()))
    for j in data[1:]:
        graph[i].append(j)

ans = True
for i in range(1,n+1):
    if sum(bfs(i,graph))!=n:
        ans = False
        break

if ans:
    print('possible')
else:
    print('impossible')
