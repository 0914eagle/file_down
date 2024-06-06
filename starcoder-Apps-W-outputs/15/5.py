
from collections import deque
n=int(input())
adj=[[] for i in range(n+1)]
visited=[False]*(n+1)
for i in range(n):
    s=list(map(int,input().split()))
    if s[0]==1:
        adj[s[1]].append(s[2])
        adj[s[2]].append(s[1])
    else:
        visited=[False]*(n+1)
        q=deque()
        q.append(s[1])
        visited[s[1]]=True
        while(len(q)>0):
            u=q.popleft()
            for i in range(len(adj[u])):
                if visited[adj[u][i]]==False:
                    if adj[u][i]==s[2]:
                        print("YES")
                        break
                    q.append(adj[u][i])
                    visited[adj[u][i]]=True
            if visited[s[2]]==True:
                break
        if visited[s[2]]==False:
            print("NO")
