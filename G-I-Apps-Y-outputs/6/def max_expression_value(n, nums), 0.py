
def max_expression_value(n, nums):
    total_sum = sum(nums)
    prefix_sums = [0] * n
    prefix_sums[0] = nums[0] ** 2

    for i in range(1, n):
        prefix_sums[i] = prefix_sums[i - 1] + nums[i] ** 2

    max_val = prefix_sums[-1] * (total_sum - nums[0])

    for i in range(1, n - 1):
        max_val = max(max_val, prefix_sums[i] * (total_sum - sum(nums[:i+1])))

    return max_val

# Read input
n = int(input())
nums = [int(input()) for _ in range(n)]

# Output the result
print(max_expression_value(n, nums))
```
