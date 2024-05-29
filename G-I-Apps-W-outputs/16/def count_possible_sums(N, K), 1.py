
def count_possible_sums(N, K):
    MOD = 10**9 + 7

    if K == 1:
        return (N+1) % MOD

    if K == N+1:
        return (N+2) % MOD

    return ((K * (N+2-K) + 1) % MOD)

# Input handling
N, K = map(int, input().split())

# Output
print(count_possible_sums(N, K))
