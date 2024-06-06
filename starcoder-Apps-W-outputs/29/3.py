
n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=[[] for i in range(n)]
flag=0
for i in range(n):
    if a[i]>=1:
        ans[i].append(1)
        a[i]-=1
for i in range(n):
    if a[i]>=1:
        ans[i].append(2)
        a[i]-=1
for i in range(n):
    if a[i]>=1:
        ans[i].append(3)
        a[i]-=1
for i in range(n):
    if a[i]>=1:
        ans[i].append(4)
        a[i]-=1
for i in range(n):
    if a[i]>=1:
        flag=1
if flag==1:
    print("NO")
else:
    print("YES")
    for i in range(n):
        print(*ans[i])
