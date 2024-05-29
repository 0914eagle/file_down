
def max_frogs_to_escape(n, d, frogs):
    frogs.sort(key=lambda x: (x[2], -x[0], -x[1]))  # Sort frogs by height descending, leap capacity descending, and weight descending

    dp = [0] * (n + 1)  # Initialize dynamic programming array with 0s
    dp[0] = 0  # Base case: 0 frogs can escape with maximum height 0

    for i in range(n):
        for j in range(i + 1, 0, -1):
            if frogs[i][2] + sum(f[1] for f in frogs[j-1:i]) <= d:  # Check if current frog can escape with frogs from previous set
                dp[i+1] = max(dp[i+1], dp[j] + 1)  # Update maximum number of frogs that can escape

    return max(dp)  # Return maximum number of frogs that can escape

# Input processing
n, d = map(int, input().split())
frogs = [list(map(int, input().split())) for _ in range(n)]

# Call the function
result = max_frogs_to_escape(n, d, frogs)
print(result)
```
