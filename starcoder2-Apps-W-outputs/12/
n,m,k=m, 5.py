
n,m,k=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
b=[]
for i in range(k):
    b.append(list(map(int,input().split())))
c=[0]*n
for i in range(k):
    for j in range(n):
        if a[j][b[i][1]-1]==1:
            c[j]+=1
for i in range(n):
    print(c[i],end=" ")
