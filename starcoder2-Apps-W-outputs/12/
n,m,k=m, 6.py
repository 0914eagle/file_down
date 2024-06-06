
n,m,k=map(int,input().split())
a=[[int(x) for x in input().split()] for i in range(n)]
b=[[0 for i in range(m)] for j in range(n)]
for i in range(k):
    x,y=map(int,input().split())
    b[x-1][y-1]+=1
for i in range(n):
    print(sum(b[i]),end=" ")
