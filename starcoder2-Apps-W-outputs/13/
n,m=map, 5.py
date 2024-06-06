
n,m=map(int,input().split())
a=[0]*n
b=[0]*n
ans=[]
for i in range(m):
    x,y=map(int,input().split())
    x-=1
    y-=1
    a[x]+=1
    b[y]+=1
    ans.append(n*n-a[x]-b[y]+1)
for i in ans:
    print(i,end=" ")
