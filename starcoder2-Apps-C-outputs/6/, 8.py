
from collections import deque
n,m,k = map(int,input().split())
o = list(map(int,input().split()))
c = list(map(int,input().split()))

graph = [[] for i in range(n+1)]
for i in range(1,n+1):
    a = list(map(int,input().split()))
    for j in range(1,a[0]+1):
        graph[i].append(a[j])

def bfs(s):
    visited = [False for i in range(n+1)]
    visited[s] = True
    q = deque()
    q.append(s)
    while q:
        s = q.popleft()
        for i in graph[s]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return visited

vis = bfs(1)

ans = 0
for i in o:
    if vis[i]:
        ans += 1
for i in c:
    if vis[i]:
        ans += 1

if ans == m+k:
    print(m+k-1)
else:
    print("impossible")
