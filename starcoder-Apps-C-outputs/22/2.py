
n,m,h=list(map(int,input().split()))
u=[0]*(n+1)
for i in range(n):
    u[i+1]=int(input())
c=[]
d=[]
for i in range(m):
    x,y=list(map(int,input().split()))
    c.append(x)
    c.append(y)
c=sorted(c)
for i in range(m*2):
    d.append(c[i])
    if d.count(c[i])>1:
        d.pop()
ans=[]
for i in range(len(d)):
    if (u[d[i]]+1)%h in u:
        ans.append(d[i])
print(len(ans))
for i in ans:
    print(i,end=" ")
