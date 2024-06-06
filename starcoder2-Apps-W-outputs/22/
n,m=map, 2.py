
n,m=map(int,input().split())
ans=m
for i in range(1,n):
    ans=ans*(m+1)
    ans%=1000000007
print(ans)
