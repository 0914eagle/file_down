
MOD = 998244353

def mod_inv(n):
    return pow(n, MOD-2, MOD)

def min_expected_earnings(n, c):
    c.sort(reverse=True)
    
    prefix_sum = [0] * (n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + c[i]
    
    result = [0] * n
    inv_n = mod_inv(n)
    
    for k in range(1, n+1):
        coeff = (prefix_sum[n] - prefix_sum[n-k]) * mod_inv(k) % MOD
        result[k-1] = coeff * inv_n % MOD

    return result

n = int(input())
c = list(map(int, input().split()))
result = min_expected_earnings(n, c)
print(" ".join(str(val) for val in result))
```
