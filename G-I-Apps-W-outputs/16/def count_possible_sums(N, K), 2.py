
def count_possible_sums(N, K):
    MOD = 10**9 + 7

    def power(x, y):
        if y == 0:
            return 1
        if y % 2 == 0:
            return power(x * x % MOD, y // 2)
        return x * power(x * x % MOD, y // 2) % MOD

    if K == 1:
        return N + 1

    answers = [1] * (N + 1)
    for i in range(1, N + 1):
        answers[i] = (answers[i - 1] + power(i + 1, MOD - 2)) % MOD

    result = 0
    for i in range(K, N + 2):
        result = (result + (answers[N - i + 1] - answers[i - 1] + 1) % MOD) % MOD

    return result

# Input
N, K = map(int, input().split())

# Output
print(count_possible_sums(N, K))
