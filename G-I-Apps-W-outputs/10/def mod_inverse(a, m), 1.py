
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1

    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    return x1 + m0 if x1 < 0 else x1

def solve_game(n, treasure_values):
    MOD = 998244353
    total_sum = sum(treasure_values)
    inv_n = mod_inverse(n, MOD)

    earnings = [0] * n
    for k in range(1, n + 1):
        earnings[k - 1] = (total_sum * inv_n * (k - 1)) % MOD

    return earnings

# Input reading
n = int(input())
treasure_values = list(map(int, input().split()))

result = solve_game(n, treasure_values)
print(*result)
```
