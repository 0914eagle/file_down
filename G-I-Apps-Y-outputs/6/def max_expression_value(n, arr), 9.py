
def max_expression_value(n, arr):
    max_val = float('-inf')
    prefix_sum = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    
    for k in range(1, n):
        max_val = max(max_val, (prefix_sum[k] ** 2) * (prefix_sum[n] - prefix_sum[k]))
    
    return max_val

# Read input
n = int(input())
arr = [int(input()) for _ in range(n)]

# Get max value and print
result = max_expression_value(n, arr)
print(result)
```
