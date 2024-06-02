
def max_points(n, arr):
    if n == 1:
        return arr[0]
    
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = min(arr[0], arr[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-2])
    
    return dp[n-1]

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(max_points(n, arr))
