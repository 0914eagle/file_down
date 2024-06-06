
n,m=map(int,input().split())
a=[[] for i in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    a[x].append(y)
for i in range(1,n+1):
    if len(a[i])>1:
        print(1)
        print(i)
        break
else:
    print(0)
