
n,m=map(int,input().split())
a=[[] for i in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    a[u].append(v)
    a[v].append(u)
vis=[0]*(n+1)
cnt=0
def dfs(x):
    global cnt
    vis[x]=1
    for i in a[x]:
        if vis[i]==0:
            cnt+=1
            dfs(i)
dfs(1)
print(m-cnt)
for i in range(1,n+1):
    for j in a[i]:
        if j>i:
            print(a[i].index(j)+1)
