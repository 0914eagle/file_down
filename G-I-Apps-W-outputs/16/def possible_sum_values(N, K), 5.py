
def possible_sum_values(N, K):
    MOD = 10**9 + 7
    if K == N + 1:
        return N + 1
    sum_mod_values = [0] * (N + 1)
    for i in range(1, N + 2):
        sum_mod_values[i - 1] = ((i * (i + 1)) // 2) % MOD
    result = 0
    for i in range(K, N + 2):
        result = (result + (sum_mod_values[N] - sum_mod_values[N - i] - sum_mod_values[i - 1] + 1)) % MOD
    return result

# Read input from standard input
N, K = map(int, input().split())
# Output the result
print(possible_sum_values(N, K))
```
