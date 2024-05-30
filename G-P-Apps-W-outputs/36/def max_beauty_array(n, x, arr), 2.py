
def max_beauty_array(n, x, arr):
    max_suffix = [0] * (n + 1)
    max_prefix = [0] * (n + 1)
    prefix = 0
    max_so_far = 0
    for i in range(n):
        prefix = max(arr[i], prefix + arr[i])
        max_so_far = max(max_so_far, prefix)
        max_prefix[i+1] = max_so_far

    suffix = 0
    max_so_far = 0
    for i in range(n-1, -1, -1):
        suffix = max(arr[i], suffix + arr[i])
        max_so_far = max(max_so_far, suffix)
        max_suffix[i] = max_so_far

    max_beauty = max(max(arr[i] * x, max_prefix[i] + max_suffix[i]) for i in range(n))
    return max(max_beauty, max(arr))

# Input parsing
n, x = map(int, input().split())
arr = list(map(int, input().split()))

# Call the function and print the output
print(max_beauty_array(n, x, arr))
```
