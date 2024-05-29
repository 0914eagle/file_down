
def longest_increasing_subsequence(N, A):
    mod = 1000000007
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    total_subsequences = sum(dp)
    expected_value = total_subsequences / N
    expected_mod = expected_value % mod
    
    return int(expected_mod)

# Input processing
N = int(input())
A = list(map(int, input().split()))

# Output
print(longest_increasing_subsequence(N, A))
```
