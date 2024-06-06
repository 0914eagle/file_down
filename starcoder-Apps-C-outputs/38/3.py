
#code
N,k = map(int,input().split())

ans = 0
for i in range(1,N+1):
    ans += (i**k)%(10**9+7)
print(ans%(10**9+7))

