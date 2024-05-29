
def count_possible_sums(N, K):
    MOD = 10**9 + 7
    if K == N+1:
        return K % MOD
    if K == 1:
        return (N+1) % MOD

    ans = 1
    total = pow(10, 100, MOD)
    for i in range(1, K):
        ans = (ans * (N + i) * pow(i, MOD - 2, MOD)) % MOD

    return (ans * total) % MOD

# Read input from STDIN
N, K = map(int, input().split())
print(count_possible_sums(N, K))
```
