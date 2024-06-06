
n,m,k=map(int,input().split())
a=[[0 for i in range(m)] for j in range(n)]
for i in range(n):
    a[i]=list(map(int,input().split()))
for i in range(k):
    x,y=map(int,input().split())
    for j in range(n):
        if a[j][y-1]==1 and j+1!=x:
            a[j][y-1]+=1
for i in range(n):
    print(sum(a[i])-n,end=" ")
