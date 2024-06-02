
def max_points(n, arr):
    dp = [[0] * n for _ in range(n)]
    
    for length in range(1, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if length == 1:
                dp[i][j] = arr[i]
            else:
                dp[i][j] = max(arr[i] - dp[i+1][j], arr[j] - dp[i][j-1])
    
    return sum(arr) - dp[0][n-1]

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(max_points(n, arr))
