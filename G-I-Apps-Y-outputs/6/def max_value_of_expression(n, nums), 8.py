
def max_value_of_expression(n, nums):
    prefix_sums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]
    
    max_val = 0
    for i in range(1, n):
        max_val = max(max_val, prefix_sums[i] ** 2 * (prefix_sums[n] - prefix_sums[i]))
    
    return max_val

# Get inputs
n = int(input())
nums = [int(input()) for _ in range(n)]

# Call the function and print the result
print(max_value_of_expression(n, nums))
```
