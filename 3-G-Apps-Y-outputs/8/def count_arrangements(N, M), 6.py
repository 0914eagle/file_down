
def count_arrangements(N, M):
    MOD = 10**9 + 7

    if abs(N - M) > 1:
        return 0

    if N == M:
        total = 2
        for i in range(2, N + 1):
            total = (total * i) % MOD
        return (total * total * 2) % MOD

    if N > M:
        return (count_arrangements(M, N) % MOD)

    total = 1
    for i in range(2, N + 1):
        total = (total * i) % MOD

    for i in range(2, M + 1):
        total = (total * i) % MOD

    return (total * 2) % MOD

# Read input
N, M = map(int, input().split())

# Calculate and print the result
print(count_arrangements(N, M))
