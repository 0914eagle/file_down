
def solve_longest_increasing_subseq_expected_value_modulo(N, A):
    dp = [0] * (N + 1)
    res = 0
    for i in range(1, N + 1):
        dp[i] = sum(dp[j] for j in range(i) if A[j] < A[i]) % 1000000007 + 1
        res = (res + dp[i]) % 1000000007
    return res

# Input
N = int(input())
A = list(map(int, input().split()))

# Output
print(solve_longest_increasing_subseq_expected_value_modulo(N, A))
```
