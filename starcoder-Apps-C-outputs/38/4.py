
n,k = map(int,input().split())

mod = 1000000007

ans = 0

for i in range(1,n+1):
    ans = (ans + (i ** k)) % mod

print(ans)
