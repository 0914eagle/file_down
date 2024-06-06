
n,m=map(int,input().split())
a=[[0]*n for i in range(n)]
for i in range(m):
    x,y=map(int,input().split())
    a[x-1][y-1]=1
    c=0
    for j in range(n):
        if a[x-1][j]==0:
            c+=1
    for j in range(n):
        if a[j][y-1]==0:
            c+=1
    print(c,end=" ")
