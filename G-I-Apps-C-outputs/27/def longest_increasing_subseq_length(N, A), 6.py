
def longest_increasing_subseq_length(N, A):
    mod = 1000000007

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    dp = [1] * N
    multiples = 1
    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        multiples = lcm(multiples, dp[i])

    total_seq = pow(N, N, mod)  # Total possible sequences

    expected_length = 0
    for i in range(N):
        expected_length += (multiples // dp[i])

    return expected_length * pow(total_seq, mod - 2, mod) % mod

# Reading input
N = int(input())
A = list(map(int, input().split()))

# Printing the expected value modulo 1000000007
print(longest_increasing_subseq_length(N, A))
```
