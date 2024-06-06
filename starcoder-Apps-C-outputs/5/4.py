
n=int(input())
a=list(map(int,input().split()))
for i in range(1,n-1):
    a[i]=min(a[i-1]+a[i+1],a[i])
print(sum(a))
