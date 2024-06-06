
n,k=map(int,input().split())
a=[list(map(int,input().split()))for i in range(n)]

d=0
for i in a:
    if i.count(1)<=k/2:
        d+=1
if d==n:
    print("YES")
else:
    print("NO")
