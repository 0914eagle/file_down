
MOD = 998244353

def ways_to_complete_figure(N, d):
    ans = 1
    sum_d = sum(d)
    for i in range(1, N):
        ans = ans * i % MOD
    for i in range(1, sum_d + 1):
        ans = ans * i % MOD
    for i in d:
        for j in range(1, i):
            ans = ans * pow(j, MOD-2, MOD) % MOD
    return ans

N = int(input())
d = list(map(int, input().split()))

print(ways_to_complete_figure(N, d))
```
