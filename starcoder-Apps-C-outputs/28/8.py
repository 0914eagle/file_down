
n,k=map(int,input().split())
m=list(map(int,input().split()))
c=0
for i in range(n):
    if m[i]==0:
        c+=1
if c==n:
    print("YES")
else:
    print("NO")
