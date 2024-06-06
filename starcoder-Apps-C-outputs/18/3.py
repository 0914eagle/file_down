
for _ in range(int(input())):
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
vis=[0]*501
for i in range(n):
for j in range(501):
if vis[j]==1:
if j+a[i]<=k:
vis[j+a[i]]=1
if j-a[i]>=0:
vis[j-a[i]]=1
print(vis.count(1))
