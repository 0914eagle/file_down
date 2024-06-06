
def solve(N, K):
    if N == 1:
        return 1 if K == 0 else 0
    if K > N * (N - 1) // 2:
        return 0
    elif K == 0:
        return pow(2, N - 1, M)
    elif N == 2:
        return K
    return sum(
        [(-1) ** (N - i) * solve(N - i + 1, K - i * (N - i)) for i in range(1, N + 1)]
    ) % M


M = 1000000007
N, K = map(int, input().split())
print(solve(N, K))
