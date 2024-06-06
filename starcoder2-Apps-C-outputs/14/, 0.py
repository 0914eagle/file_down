
n,r=map(int,input().split())
d={}
for i in range(r):
    a,b,c=map(int,input().split())
    if a not in d:
        d[a]={}
    if b not in d:
        d[b]={}
    d[a][b]=c
    d[b][a]=c
f=int(input())
for i in range(f):
    a,b,c=map(int,input().split())
    if a not in d:
        d[a]={}
    if b not in d:
        d[b]={}
    d[a][b]=c
    d[b][a]=c

def dijkstra(s):
    dist=[float('inf')]*(n+1)
    dist[s]=0
    q=[s]
    while q:
        u=q.pop(0)
        for v in d[u]:
            if dist[v]>dist[u]+d[u][v]:
                dist[v]=dist[u]+d[u][v]
                q.append(v)
    return dist

dist=dijkstra(1)
print(dist[1])
