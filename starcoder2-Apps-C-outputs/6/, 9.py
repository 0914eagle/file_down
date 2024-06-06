
n,m,k=map(int,input().split())
o=list(map(int,input().split()))
c=list(map(int,input().split()))
g=[[] for i in range(n+1)]
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(1,a[0]+1):
        g[i+1].append(a[j])

def bfs(x):
    q=[x]
    vis=[0]*(n+1)
    vis[x]=1
    while q:
        t=q.pop(0)
        for i in g[t]:
            if vis[i]==0:
                vis[i]=1
                q.append(i)
    return vis

vis=bfs(1)
ans=0
for i in o:
    if vis[i]==1:
        ans+=1
for i in c:
    if vis[i]==1:
        ans+=1
if ans==m+k:
    print(m+k-1)
else:
    print("impossible")
