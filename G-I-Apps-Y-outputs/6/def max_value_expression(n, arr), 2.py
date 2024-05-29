
def max_value_expression(n, arr):
    prefix_sums = [0] * n
    prefix_sums[0] = arr[0]
    
    for i in range(1, n):
        prefix_sums[i] = prefix_sums[i - 1] + arr[i]
    
    max_val = float('-inf')
    
    for k in range(n - 1):
        val = (prefix_sums[k] ** 2) * (prefix_sums[-1] - prefix_sums[k])
        max_val = max(max_val, val)
    
    return max_val

# Read input
n = int(input())
arr = [int(input()) for _ in range(n)]

# Call the function and print the result
print(max_value_expression(n, arr))
```
