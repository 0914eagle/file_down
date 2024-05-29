
def possible_sum_values(N, K):
    MOD = 10**9 + 7

    if K == 1:
        return (N+1) % MOD
    elif K == N+1:
        return 1

    # Calculate (N+1) choose K
    fact = [1]
    for i in range(1, N+2):
        fact.append((fact[-1] * i) % MOD)
    inv_fact = [pow(fact[-1], MOD-2, MOD)]
    for i in range(N+1, 0, -1):
        inv_fact.append((inv_fact[-1] * i) % MOD)
    inv_fact = inv_fact[::-1]

    def choose(n, k):
        return (fact[n] * inv_fact[k] * inv_fact[n-k]) % MOD

    result = 0
    for i in range(K, N+2):
        result = (result + choose(N+1, i)) % MOD

    return result

# Read input values
N, K = map(int, input().split())

# Calculate and print number of possible sum values
print(possible_sum_values(N, K))
```
