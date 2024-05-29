
MOD = 998244353

def inverse_mod(a):
    return pow(a, MOD - 2, MOD)

def solve_game(n, treasure):
    treasure.sort()
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + treasure[i - 1]

    ans = [0] * n
    for k in range(1, n + 1):
        sum_treasure = prefix_sum[k]
        sum_inverse = inverse_mod(k)
        ans[k - 1] = (sum_treasure * sum_inverse) % MOD

    return ans

# Input
n = int(input())
treasure = list(map(int, input().split()))

# Output
result = solve_game(n, treasure)
print(*result)
```
