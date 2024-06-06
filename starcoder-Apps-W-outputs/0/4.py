
# cook your dish here
from collections import defaultdict
n,m=map(int,input().split())
E=[int(i) for i in input().split()]
G=defaultdict(set)
for i in range(m):
    t1,t2=map(int,input().split())
    G[t1].add(t2)
res=0
v=0
vis=[0]*n
for i in range(n):
    if E[i]==1:
        if vis[i]==0:
            vis[i]=1
            v=1
        for j in G[i]:
            if vis[j]==0:
                vis[j]=1
                v=1
        if v:
            res+=1
            v=0
print(res)
