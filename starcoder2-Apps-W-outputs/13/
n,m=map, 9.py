
n,m=map(int,input().split())
l=[0]*(n+1)
for i in range(m):
    x,y=map(int,input().split())
    l[x]+=1
    l[y]+=1
    print((n-l[x])*(n-l[y]),end=" ")
