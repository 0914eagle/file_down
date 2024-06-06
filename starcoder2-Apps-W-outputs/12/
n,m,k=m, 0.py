
n,m,k=map(int,input().split())
a=[[int(i) for i in input().split()] for j in range(n)]
b=[[int(i) for i in input().split()] for j in range(k)]
c=[0]*n
for i in range(k):
    for j in range(n):
        if a[j][b[i][1]-1]==1:
            c[j]+=1
for i in range(n):
    print(c[i],end=" ")
