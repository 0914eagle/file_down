
n,m,k=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(k):
    x,y=map(int,input().split())
    for j in range(n):
        if a[j][y-1]==1 and j!=x-1:
            a[j][y-1]=2
for i in range(n):
    print(a[i].count(2),end=" ")
