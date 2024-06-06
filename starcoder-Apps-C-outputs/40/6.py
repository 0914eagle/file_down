
import sys
sys.setrecursionlimit(10**6)
def dfs(u):
    global ans
    visited[u]=1
    for i in graph[u]:
        if not visited[i]:
            dfs(i)
    ans=max(ans,len(graph[u]))
n=int(input())
graph=[[] for _ in range(n)]
visited=[0 for _ in range(n)]
for i in range(n):
    a,b=map(int,input().split())
    if i!=0:
        graph[b].append(i)
ans=0
dfs(0)
print(ans)
