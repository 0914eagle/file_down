
from math import factorial

def longest_increasing_subsequence_length(N, A):
    MOD = 1000000007
    inv_fact = [pow(factorial(N), MOD-2, MOD) for _ in range(N+1)]
    
    def pow_mod(a, b):
        res = 1
        while b:
            if b % 2:
                res = (res * a) % MOD
            a = (a * a) % MOD
            b //= 2
        return res
    
    expected = 0
    for i in range(1, N+1):
        numerator = 1
        for j in range(1, N+1):
            numerator = (numerator * (A[j-1] - i + 1) * inv_fact[i-1]) % MOD
        expected += (numerator * inv_fact[N]) % MOD
    
    return expected % MOD

# Input handling
N = int(input())
A = list(map(int, input().split()))

result = longest_increasing_subsequence_length(N, A)
print(result)
```
