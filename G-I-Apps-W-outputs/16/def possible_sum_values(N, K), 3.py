
def possible_sum_values(N, K):
    MOD = 10**9 + 7
    if K == 1:
        return N+1
    
    if K > N-K:
        K = N-K
    
    ans = 1
    numerator = 1
    denominator = 1

    for i in range(K):
        numerator = (numerator * (N - i)) % MOD
        denominator = (denominator * (i + 1)) % MOD

    inv_denominator = pow(denominator, MOD - 2, MOD)

    ans = (numerator * inv_denominator) % MOD
    return ans

# Input reading
N, K = map(int, input().split())
print(possible_sum_values(N, K))
```
