
MOD = 998244353

def solve_figure_complete(N, d):
    ans = 1
    factor = 1
    for i in range(1, N+1):
        ans = (ans * (factor * 2 - 1)) % MOD
        factor = (factor + d[i-1]) % MOD
    return ans

N = int(input())
d = list(map(int, input().split()))
print(solve_figure_complete(N, d))
```
