
# Code1:
n,m=map(int,input().split())
ans=0
for i in range(n):
    a=input()
    ans+=sum(1 if a[j]==chr(ord('A')+j) else 0 for j in range(m))
print(ans)


# Code2:
n,m=map(int,input().split())
ans=0
for i in range(m):
    a=input()
    ans+=sum(a[j]=='A' for j in range(n))
print(ans)
