
n, k = map(int, input().split())
h = list(map(int, input().split()))

MOD = 998244353

ans = pow(k, n, MOD)

for i in range(n):
    if h[i] != h[(i+1)%n]:
        ans = (ans - pow(k-1, n, MOD) + MOD) % MOD

print(ans)

