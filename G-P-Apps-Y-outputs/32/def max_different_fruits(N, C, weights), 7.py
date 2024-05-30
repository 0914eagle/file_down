
def max_different_fruits(N, C, weights):
    dp = [0] * (C+1)
    
    for weight in weights:
        for i in range(C, weight-1, -1):
            dp[i] = max(dp[i], dp[i-weight] + 1)
    
    return dp[C]

# Input parsing
input_line = input().split()
N = int(input_line[0])
C = int(input_line[1])

weights = list(map(int, input().split()))

# Call the function and output the result
print(max_different_fruits(N, C, weights))
```
