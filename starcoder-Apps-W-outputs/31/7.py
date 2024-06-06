
n=int(input())
x=input().split()
a=[0]*n
ans=0
for i in range(n):
    a[int(x[i])-1]=i
for i in range(1,n):
    ans+=abs(a[i]-a[i-1])
print(ans)

