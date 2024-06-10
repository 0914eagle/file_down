
n,k=map(int,input().split())
a=list(map(int,input().split()))
m=100000000000000000000
s=0
for i in a:
    if i<m:
        m=i
    s+=i
print(s-m*k-100)

