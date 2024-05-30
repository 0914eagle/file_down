
def max_beauty_array(n, x, a):
    def max_sum(arr):
        max_sum_val = curr_sum = 0
        for num in arr:
            curr_sum = max(num, curr_sum + num)
            max_sum_val = max(max_sum_val, curr_sum)
        return max_sum_val
    
    original_max_sum = max_sum(a)
    
    if x == 0:
        return original_max_sum

    # Case 1: Try multiplying the entire array with x
    max_sum_with_x = max_sum(a) * x

    # Case 2: Try multiplying each prefix and suffix separately
    prefix_sums = [0] + list(a)
    suffix_sums = list(a) + [0]
    for i in range(1, n + 1):
        prefix_sums[i] += prefix_sums[i - 1]
        suffix_sums[n - i] += suffix_sums[n - i + 1]
    
    max_sum_with_prefix_suffix = max(max(prefix_sums[i] * x + max_sum(suffix_sums[i + 1:]) for i in range(n)),
                                     max(max_sum(prefix_sums[:i]) + suffix_sums[i] * x for i in range(1, n + 1)))
    
    return max(original_max_sum, max_sum_with_x, max_sum_with_prefix_suffix)

# Read input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(max_beauty_array(n, x, a))
```
