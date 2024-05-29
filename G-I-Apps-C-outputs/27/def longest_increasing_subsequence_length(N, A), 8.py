
def longest_increasing_subsequence_length(N, A):
    mod = 1000000007

    # Initialize dp array to store the maximum length at each index
    dp = [1] * N

    for i in range(1, N):
        for j in range(i):
            if A[i] >= A[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Calculate the expected value
    total_sum = sum(dp)
    expected_value = total_sum // N

    # Print the expected value modulo 1000000007
    print(expected_value % mod)

# Read input
N = int(input())
A = list(map(int, input().split()))

# Call the function
longest_increasing_subsequence_length(N, A)
