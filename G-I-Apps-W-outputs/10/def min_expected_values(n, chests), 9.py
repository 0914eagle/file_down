
def min_expected_values(n, chests):
    MOD = 998244353
    
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + chests[i]
    
    max_inv = [0] * (n + 1)
    min_inv = [0] * (n + 1)
    for k in range(1, n + 1):
        max_inv[k] = pow(k, MOD - 2, MOD)
        min_inv[k] = pow(n - k + 1, MOD - 2, MOD)
    
    result = [0] * n
    for k in range(1, n + 1):
        q = (prefix_sum[n] - prefix_sum[k - 1]) % MOD
        result[k - 1] = (q * min_inv[k]) % MOD
    
    return result

n = int(input())
chests = list(map(int, input().split()))

output = min_expected_values(n, chests)
print(*output)
```
