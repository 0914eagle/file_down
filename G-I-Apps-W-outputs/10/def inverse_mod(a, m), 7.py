= 998244353

def inverse_mod(a, m):
    m0 = m
    x0, x1 = 0, 1
    
    if m == 1:
        return 0
    
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
        
    if x1 < 0:
        x1 += m0
        
    return x1

def solve_level(n, treasure_values):
    total_sum = sum(treasure_values)
    prefix_sums = [0]
    
    for i in range(1, n + 1):
        prefix_sums.append(prefix_sums[-1] + treasure_values[i - 1])
    
    result = []
    inv_n = inverse_mod(n, MOD)
    
    for k in range(1, n + 1):
        coeff = (total_sum - prefix_sums[n - k]) % MOD
        coeff = (coeff * inverse_mod(n - k + 1, MOD)) % MOD
        result.append((coeff * inv_n) % MOD)
    
    return result

n = int(input())
treasure_values = list(map(int, input().split()))

result = solve_level(n, treasure_values)
print(" ".join(str(val) for val in result))
