
n,m=map(int,input().split())
a=list(map(int,input().split()))
l=[]
r=[]
for i in range(m):
    x,y=map(int,input().split())
    l.append(x)
    r.append(y)
ans=0
for i in range(m):
    cnt=0
    for j in range(l[i]-1,r[i]):
        cnt+=a[j]
    ans=max(ans,cnt)
print(ans)
