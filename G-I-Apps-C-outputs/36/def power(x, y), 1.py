
MOD = 998244353

def power(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) ** 2 % MOD
    else:
        return power(x, y // 2) ** 2 * x % MOD

def solve(N, d):
    result = 1
    total = 0
    for i in range(N):
        result = (result * (total + 1)) % MOD
        total += d[i]
    return result

N = int(input())
d = list(map(int, input().split()))
print(solve(N, d))
```
