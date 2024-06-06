
n,m,k=map(int,input().split())
a=[[0 for i in range(m)] for j in range(n)]
for i in range(n):
    a[i]=list(map(int,input().split()))
b=[0 for i in range(n)]
for i in range(k):
    x,y=map(int,input().split())
    x-=1
    y-=1
    for j in range(n):
        if a[j][y]==1 and j!=x:
            b[j]+=1
for i in range(n):
    print(b[i],end=" ")
