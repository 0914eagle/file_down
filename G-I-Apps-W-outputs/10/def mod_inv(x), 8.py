
MOD = 998244353

def mod_inv(x):
    return pow(x, MOD - 2, MOD)

def solve(n, chests):
    chests.sort()
    
    prefix_sum = [0]
    for i in range(n):
        prefix_sum.append(prefix_sum[-1] + chests[i])

    ans = [0] * n
    for k in range(1, n + 1):
        summation = 0
        for i in range(n - k, n):
            summation += chests[i]
        ans[k - 1] = (summation * mod_inv(n)) % MOD

    return ans

n = int(input())
chests = list(map(int, input().split()))

result = solve(n, chests)
print(*result)
```
