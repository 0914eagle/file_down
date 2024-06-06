
n,m=map(int,input().split())
l=[0]*n
for i in range(m):
    x,y=map(int,input().split())
    l[x-1]+=1
    l[y-1]+=1
    print((n*n)-(n+n-l[x-1]-l[y-1]))
