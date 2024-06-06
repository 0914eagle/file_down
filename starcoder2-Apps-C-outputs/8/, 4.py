
n,m=map(int,input().split())
g=[[] for i in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    g[u-1].append(v-1)
vis=[0]*n
def dfs(u):
    vis[u]=1
    for v in g[u]:
        if vis[v]==0:
            dfs(v)
        elif vis[v]==1:
            print(0)
            exit()
    vis[u]=2
for i in range(n):
    if vis[i]==0:
        dfs(i)
print(m-n)
for i in range(1,n+1):
    print(i)
