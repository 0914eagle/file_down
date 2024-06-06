
n,m = map(int,input().split())
ans = 0
for i in range(1,m+1):
    ans += pow(m,n,10**9+7)
print(ans%(10**9+7))
