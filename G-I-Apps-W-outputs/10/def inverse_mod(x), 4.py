
MOD = 998244353

def inverse_mod(x):
    return pow(x, MOD - 2, MOD)

def solve(n, treasures):
    treasure_sum = sum(treasures)
    prefix_sum = [0] * (2 * n + 1)
    for i in range(1, 2 * n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + treasures[(i - 1) % n]

    result = [0] * n
    inv_n = inverse_mod(n)
    for k in range(1, n + 1):
        min_expected = 0
        for i in range(k, n + k):
            left_sum = prefix_sum[i] - prefix_sum[i - k]
            right_sum = prefix_sum[n] - left_sum
            expected_value = min(left_sum, right_sum) + max(left_sum, right_sum) * inv_n
            min_expected += expected_value

        result[k - 1] = (min_expected * inverse_mod(n)) % MOD

    return result

# Input
n = int(input())
treasures = list(map(int, input().split()))

# Output
output = solve(n, treasures)
print(*output)
```
