
n,k=map(int,input().split())
cnt=0
for _ in range(n):
    x=list(map(int,input().split()))
    if sum(x)>k//2:
        cnt+=1
if cnt==0:
    print("YES")
else:
    print("NO")
