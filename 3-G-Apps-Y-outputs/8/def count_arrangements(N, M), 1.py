
def count_arrangements(N, M):
    MOD = 10**9 + 7

    if abs(N - M) > 1:
        return 0

    if N == M:
        total = 2
        for i in range(2, N + 1):
            total = (total * i) % MOD
        return (total * total * 2) % MOD
    else:
        total = 1
        for i in range(2, min(N, M) + 1):
            total = (total * i) % MOD
        return (total * total * max(N, M)) % MOD

# Input
N, M = map(int, input().split())

# Output
print(count_arrangements(N, M))
