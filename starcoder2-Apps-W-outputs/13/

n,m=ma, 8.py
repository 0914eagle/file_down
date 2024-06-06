

n,m=map(int,input().split())
a=[0]*(n+1)
b=[0]*(n+1)
for i in range(m):
    x,y=map(int,input().split())
    a[x]+=1
    b[y]+=1
ans=n*n
for i in range(1,n+1):
    ans-=a[i]+b[i]-1
print(ans)

