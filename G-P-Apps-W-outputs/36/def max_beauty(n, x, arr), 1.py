
def max_beauty(n, x, arr):
    prefix_max = [0] * (n + 1)
    suffix_max = [0] * (n + 1)
    curr_max = 0
    total_sum = 0
    
    for i in range(1, n + 1):
        total_sum += arr[i - 1]
        curr_max = max(curr_max + arr[i - 1], arr[i - 1])
        prefix_max[i] = max(prefix_max[i - 1], curr_max)
    
    curr_max = 0
    for i in range(n, 0, -1):
        curr_max = max(curr_max + arr[i - 1], arr[i - 1])
        suffix_max[i] = max(suffix_max[i + 1], curr_max)
    
    beauty = 0
    for i in range(1, n + 1):
        beauty = max(beauty, max(0, prefix_max[i - 1]) + x * total_sum + max(0, suffix_max[i]))
    
    return beauty

# Input
n, x = map(int, input().split())
arr = list(map(int, input().split()))

# Output
print(max_beauty(n, x, arr))
```
