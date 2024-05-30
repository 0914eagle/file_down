
def max_beauty_array(n, x, a):
    def max_subarray_sum(arr):
        max_ending_here = max_so_far = 0
        for num in arr:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    original_sum = max_subarray_sum(a)
    modified_sum = max_subarray_sum([num if num > 0 else num * x for num in a])

    return max(original_sum, modified_sum)

# Input processing
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output
print(max_beauty_array(n, x, a))
```
