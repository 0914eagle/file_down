
def max_points(n, sequence):
    points = [0] * (max(sequence) + 1)
    for num in sequence:
        points[num] += num
    
    dp = [0] * (max(sequence) + 1)
    dp[0] = points[0]
    dp[1] = max(points[0], points[1])
    
    for i in range(2, len(dp)):
        dp[i] = max(dp[i-1], dp[i-2] + points[i])
    
    return dp[-1]

# Input parsing
n = int(input())
sequence = list(map(int, input().split()))

# Call the function and print the result
print(max_points(n, sequence))
```
