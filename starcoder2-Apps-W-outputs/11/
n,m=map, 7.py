
n,m=map(int,input().split())
a=list(map(int,input().split()))
s=0
for i in range(m):
    l,r=map(int,input().split())
    s+=sum(a[l-1:r])
print(s)
