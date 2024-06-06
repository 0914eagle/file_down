
n,m=map(int,input().split())
graph=[[] for i in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    graph[u-1].append(v-1)

def dfs(node,parent):
    visited[node]=True
    for child in graph[node]:
        if not visited[child]:
            dfs(child,node)
        elif child!=parent:
            print(1)
            print(graph[node].index(child)+1)
            exit()

visited=[False]*n
for i in range(n):
    if not visited[i]:
        dfs(i,-1)
print(0)
