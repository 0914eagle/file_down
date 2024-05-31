
def pluck(arr):
    even_values = [x for x in arr if x % 2 == 0]
    if not even_values:
        return []

    min_even_value = min(even_values)
    min_index = float('inf')
    result = []

    for i, val in enumerate(arr):
        if val == min_even_value and i < min_index:
            min_index = i
            result = [val, i]

    return result

# Test cases
print(pluck([4, 2, 3]))  # Output: [2, 1]
print(pluck([1, 2, 3]))  # Output: [2, 1]
print(pluck([]))  # Output: []
print(pluck([5, 0, 3, 0, 4, 2]))  # Output: [0, 1]
```
