
n,m,k=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]
b=[0 for i in range(n)]
for i in range(k):
    x,y=map(int,input().split())
    for j in range(n):
        if a[j][y-1]==1 and j!=x-1:
            b[j]+=1
for i in b:
    print(i,end=" ")
