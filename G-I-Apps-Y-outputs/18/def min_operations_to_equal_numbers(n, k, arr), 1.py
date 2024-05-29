
def min_operations_to_equal_numbers(n, k, arr):
    freq_dict = {}
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    min_operations = float('inf')
    for num in freq_dict:
        temp_operations = 0
        count = freq_dict[num]
        while count < k:
            count *= 2
            temp_operations += 1
        min_operations = min(min_operations, temp_operations)

    return min_operations

# Input parsing
n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(min_operations_to_equal_numbers(n, k, arr))
```
