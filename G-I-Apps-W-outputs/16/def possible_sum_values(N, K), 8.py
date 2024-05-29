
def possible_sum_values(N, K):
    MOD = 10**9 + 7
    start = 10**100 % MOD
    end = (10**100 + N) % MOD
    total_sum_values = end - start + 1

    if K == 1:
        return total_sum_values

    binomial_memo = [1] * (N + 2)
    for i in range(2, N + 2):
        binomial_memo[i] = (binomial_memo[i - 1] * (K - 1 + i) * pow(i, MOD - 2, MOD)) % MOD

    answer = 0
    for i in range(K, N + 2):
        answer = (answer + binomial_memo[i] * total_sum_values) % MOD

    return answer

# Input processing
N, K = map(int, input().split())

# Output
print(possible_sum_values(N, K))
