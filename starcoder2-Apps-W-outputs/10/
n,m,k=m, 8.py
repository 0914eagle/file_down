
n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort()
b.sort()
c.sort()
ans=0
cost=0
for i in range(n):
    if a[i]<b[i]:
        ans+=1
        cost+=a[i]
for i in range(m):
    if b[i]<c[i]:
        ans+=1
        cost+=b[i]
for i in range(k):
    if c[i]<b[i]:
        ans+=1
        cost+=c[i]
print(ans,cost)
