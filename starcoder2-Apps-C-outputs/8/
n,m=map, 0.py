
n,m=map(int,input().split())
a=[0]*(n+1)
for i in range(m):
    x,y=map(int,input().split())
    a[x]+=1
    a[y]+=1
for i in range(1,n+1):
    if a[i]%2==1:
        print(0)
        break
else:
    print(m-n+1)
    for i in range(1,n+1):
        print(i)
