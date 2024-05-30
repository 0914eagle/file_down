
def expected_unique_elements(n, arr):
    prefix_count = [0] * (max(arr) + 1)
    total_unique = 0
    
    for num in arr:
        if prefix_count[num] == 0:
            total_unique += 1
        prefix_count[num] += 1
    
    expected_value = 0
    for i in range(1, len(prefix_count)):
        expected_value += i * (prefix_count[i] / n) * total_unique
    
    return expected_value

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
result = expected_unique_elements(n, arr)
print("{:.6f}".format(result))
```
